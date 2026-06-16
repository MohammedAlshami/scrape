"""
Run 3 GE16 prediction agents using pre-built document index + OpenRouter GPT-5-nano.
Agents: Support (Jul-Sep 2027), Against (2026), Neutral

Usage: python scrape/run_agents.py
"""

import os, sys, json, pickle, time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_DIR = os.path.join(ROOT, "data", ".doc_index")
RESULTS_DIR = os.path.join(ROOT, "data", "agent_results")
os.makedirs(RESULTS_DIR, exist_ok=True)

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            OPENROUTER_KEY = f.read().strip().split("=", 1)[1].strip()

# ============================================================
# LOAD PRE-BUILT INDEX
# ============================================================
print("Loading pre-built document index...")
with open(os.path.join(INDEX_DIR, "chunks.pkl"), "rb") as f:
    chunks = pickle.load(f)
with open(os.path.join(INDEX_DIR, "sources.pkl"), "rb") as f:
    sources = pickle.load(f)
with open(os.path.join(INDEX_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)
with open(os.path.join(INDEX_DIR, "matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)
print(f"Loaded {len(chunks)} chunks from index")

# ============================================================
# RETRIEVAL
# ============================================================
def retrieve(query, k=8):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_indices = np.argsort(scores)[-k:][::-1]
    
    results = []
    seen_sources = set()
    for idx in top_indices:
        if scores[idx] > 0:
            src = sources[idx]
            results.append({
                "source": src,
                "score": round(float(scores[idx]), 3),
                "text": chunks[idx][:2000]
            })
            seen_sources.add(src)
    return results

# ============================================================
# OPENROUTER LLM
# ============================================================
def query_llm(system_prompt, user_message, max_tokens=4000, retries=2):
    body = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }
    
    for attempt in range(retries):
        try:
            resp = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json=body,
                headers={
                    "Authorization": f"Bearer {OPENROUTER_KEY}",
                    "Content-Type": "application/json",
                },
                timeout=120,
            )
            if resp.status_code == 200:
                content = resp.json()["choices"][0]["message"]["content"]
                if content:
                    return content
                else:
                    print(f"  [WARN] Empty response, retry {attempt+1}/{retries}")
            else:
                print(f"  [WARN] API {resp.status_code}, retry {attempt+1}/{retries}: {resp.text[:200]}")
        except Exception as e:
            print(f"  [WARN] Exception, retry {attempt+1}/{retries}: {e}")
        
        if attempt < retries - 1:
            time.sleep(5 * (attempt + 1))
    
    return "[Analysis could not be completed due to API errors]"

# ============================================================
# RESEARCH PHASE
# ============================================================
RESEARCH_QUERIES = [
    "GE16 election timing prediction 2026 2027 Malaysia",
    "Anwar Ibrahim approval rating government popularity",
    "Malaysia fuel subsidy cost budget deficit spending",
    "Iran war oil price impact Petronas dividend Malaysia",
    "snap election Malaysia early general election speculation",
    "PH BN coalition collapse fracture state election 2026",
    "PAS BERSATU split opposition fragmentation WAWASAN BERSAMA",
    "historical campaign duration dissolution polling Malaysia",
    "by-election trend vote swing government opposition",
    "redelineation boundary review Malaysia 2026 2027",
    "Oust Anwar rally protest subsidy reform backlash",
    "monsoon flood season election window Malaysia",
    "constitution Article 55 parliament dissolution deadline",
    "Malaysia Johor state election 2026 bellwether",
    "Negeri Sembilan state election 2026 PH BN contest",
    "Malaysia GDP growth unemployment rate economy 2026",
    "BNM OPR interest rate inflation ringgit exchange rate",
    "Undi18 voter registration youth vote impact",
    "Anwar statement no early election full term",
    "Malaysia general election historical PM timing",
]

def research_phase(agent_name):
    print(f"  Researching...")
    context = ""
    for q in RESEARCH_QUERIES[:10]:  # Use top 10 queries
        results = retrieve(q)
        for r in results[:5]:  # Top 5 per query
            context += f"\n--- Source: {r['source']} (score: {r['score']}) ---\n{r['text'][:1000]}\n"
        time.sleep(0.2)
    return context[:25000]  # Keep manageable for model

# ============================================================
# AGENT DEFINITIONS
# ============================================================
AGENTS = {
    "support": {
        "name": "Supporter",
        "system": """You are a Malaysian election analyst who BELIEVES GE16 will be held in July-September 2027.
Your job is to find evidence that supports this prediction from the provided context.
Arguments to consider:
- Anwar wants full term (deadline Feb 2028). He said "tunggu pilihan raya dua tahun lagi" in Jul 2025
- Jul-Sep 2027 is best weather (SW monsoon, no major festivals)
- After state elections: Malacca ~Feb 27, Sarawak ~Apr 27, Johor ~Jun 27
- Redelineation not done (eligible after Mar 2026, takes time)
- Economy needs time to stabilize post-Iran war
- Anwar's approval is recovering (50%->55%), waiting lets it rise further
- PN is already fragmented (PAS-BERSATU split), no need to rush
- Parliament sessions scheduled through Dec 2026 suggest no early dissolution

Cite specific source filenames. Be thorough and decisive."""
    },
    "against": {
        "name": "Opposer",
        "system": """You are a Malaysian election analyst who BELIEVES GE16 will be HELD IN 2026, not Jul-Sep 2027.
Arguments to consider:
- Iran war oil spike is temporary; peace deal will crash oil prices → call while revenue high
- RON95 subsidy removal pending → call BEFORE voters feel the pain
- Opposition fragmented (PAS-BERSATU split, WAWASAN forming) → strike while weak
- PH-BN pact fraying (Johor BN going solo) → may not survive until 2027
- Oust Anwar rally (Jul 2025) showed vulnerability → seek fresh mandate
- Rafizi's BERSAMA needs time → call before they organize
- Historical pattern: Malaysian PMs call elections BEFORE unpopular reforms hit
- Anwar can campaign on decent GDP (~5%), low unemployment, ringgit recovering

Cite specific source filenames. Be thorough and decisive."""
    },
    "neutral": {
        "name": "Neutral",
        "system": """You are a NEUTRAL Malaysian election analyst. Weigh ALL evidence objectively.
Consider BOTH sides:
FOR Jul-Sep 2027: Best weather, after state elections, redelineation, Anwar prefers full term
FOR 2026: Oil revenue peak, subsidy pain not yet felt, opposition fragmented, PH-BN may collapse

You must:
1. Summarize strongest arguments for BOTH positions
2. Weight them by evidence quality
3. Give final probability assessment (e.g. 60% 2027, 40% 2026)
4. Acknowledge uncertainties that could change outcome
5. Be decisive — pick a most likely scenario

Cite specific source filenames."""
    },
}

# ============================================================
# RUN ALL AGENTS
# ============================================================
print("\n" + "=" * 60)
print("RUNNING 3 GE16 PREDICTION AGENTS")
print("Model: gpt-5-nano with high reasoning")
print("=" * 60)

for agent_id, info in AGENTS.items():
    print(f"\n\n{'='*60}")
    print(f"AGENT: {info['name']} ({agent_id})")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    # Research phase
    print(f"[Phase 1] Researching from 6,777 indexed documents...")
    context = research_phase(info["name"])
    print(f"  Collected {len(context)} chars of relevant context")
    
    # Analysis phase
    print(f"[Phase 2] Analyzing with GPT-5-nano (high reasoning)...")
    analysis = query_llm(
        info["system"],
        f"""Based on the following research context, analyze when GE16 will be held.

CONTEXT:
{context}

Provide your analysis with:
1. Your predicted timeframe (month/year)
2. Probability estimate
3. Top 5 evidence points with source filenames
4. Top 3 counter-arguments and why you dismiss them
5. What would change your mind"""
    )
    elapsed = time.time() - start_time
    print(f"  Analysis completed in {elapsed:.0f}s")
    
    # Final refinement with additional context
    print(f"[Phase 3] Final deliberation...")
    more_context = retrieve("Anwar statement full term opposition fragmentation Malaysia election 2026", k=10)
    extra_ctx = ""
    for r in more_context:
        extra_ctx += f"\n--- Source: {r['source']} ---\n{r['text']}\n"
    
    final = query_llm(
        info["system"],
        f"""Your previous analysis:
{analysis}

Additional context:
{extra_ctx[:15000]}

What is your FINAL GE16 prediction? Be decisive with specific probabilities."""
    )
    
    total_time = time.time() - start_time
    
    # Save result
    result = f"""# Agent: {info['name']}
# Model: gpt-5-nano (high reasoning)
# Runtime: {total_time:.0f}s
# Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

## Initial Analysis
{analysis}

## Final Verdict
{final}
"""
    
    result_path = os.path.join(RESULTS_DIR, f"agent_{agent_id}_{int(time.time())}.md")
    with open(result_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    print(f"\n{'='*60}")
    print(f"AGENT {info['name'].upper()} COMPLETE ({total_time:.0f}s)")
    print(f"Saved: {os.path.relpath(result_path, ROOT)}")
    print(f"{'='*60}")
    if final:
        print(final[:500])

print(f"\n\n{'='*60}")
print("ALL 3 AGENTS COMPLETE")
print(f"Results saved to: {RESULTS_DIR}")
print(f"{'='*60}")
