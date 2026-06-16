"""
LangChain RAG Agent System for GE16 Prediction
Three agents: Support, Against, Neutral
Uses OpenRouter + our data files for RAG.
"""

import os, sys, glob, json, time, textwrap

from langchain_community.document_loaders import TextLoader, CSVLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
INSIGHTS = os.path.join(ROOT, "insights")
CHROMA_DIR = os.path.join(ROOT, "data", ".chroma_db")

os.environ["TOKENIZERS_PARALLELISM"] = "false"

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            OPENROUTER_KEY = f.read().strip().split("=", 1)[1].strip()

# ============================================================
# 1. LOAD ALL DATA FILES
# ============================================================
print("=" * 60)
print("LOADING DATA FILES FOR RAG...")
print("=" * 60)

all_docs = []

# Load all .md files from data/ recursively
md_files = glob.glob(os.path.join(DATA, "**", "*.md"), recursive=True)
print(f"Found {len(md_files)} .md files")

for fpath in md_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content.strip()) < 100:
            continue
        rel = os.path.relpath(fpath, ROOT)
        all_docs.append(Document(page_content=content, metadata={"source": rel}))
    except:
        pass

# Load key CSV files as text
csv_files = glob.glob(os.path.join(DATA, "**", "*.csv"), recursive=True)
for fpath in csv_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content.strip()) < 100:
            continue
        rel = os.path.relpath(fpath, ROOT)
        all_docs.append(Document(page_content=f"CSV DATA: {rel}\n{content[:50000]}", metadata={"source": rel}))
    except:
        pass

# Also load insights files
insight_files = glob.glob(os.path.join(INSIGHTS, "**", "*.md"), recursive=True)
for fpath in insight_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content.strip()) < 100:
            continue
        rel = os.path.relpath(fpath, ROOT)
        all_docs.append(Document(page_content=content, metadata={"source": rel}))
    except:
        pass

print(f"Total documents loaded: {len(all_docs)}")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
chunks = splitter.split_documents(all_docs)
print(f"Chunks created: {len(chunks)}")

# ============================================================
# 2. CREATE VECTOR STORE
# ============================================================
print("\nCreating embeddings and vector store...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_DIR)
print(f"Vector store ready with {vectordb._collection.count()} vectors")

# ============================================================
# 3. OPENROUTER LLM WRAPPER
# ============================================================
def query_openrouter(system_prompt, messages, max_tokens=2000):
    """Query OpenRouter with system + messages."""
    import requests
    
    full_messages = [{"role": "system", "content": system_prompt}]
    for m in messages:
        full_messages.append(m)
    
    body = {
        "model": "openai/gpt-4o-mini",
        "messages": full_messages,
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }
    
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
            return resp.json()["choices"][0]["message"]["content"]
        else:
            return f"[API Error {resp.status_code}: {resp.text[:200]}]"
    except Exception as e:
        return f"[Exception: {e}]"

# ============================================================
# 4. RAG RETRIEVER
# ============================================================
def retrieve_context(query, k=10):
    """Retrieve relevant context chunks."""
    results = vectordb.similarity_search(query, k=k)
    context = ""
    for i, r in enumerate(results):
        src = r.metadata.get("source", "unknown")
        context += f"\n--- Source {i+1}: {src} ---\n{r.page_content[:1500]}\n"
    return context

# ============================================================
# 5. AGENT DEFINITIONS
# ============================================================
AGENTS = {
    "support": {
        "name": "Supporter",
        "system_prompt": """You are a Malaysian election analyst who BELIEVES GE16 will be held in July-September 2027.
Your job is to find evidence from the provided context that supports this prediction.
Arguments you should consider:
- Anwar wants to serve full term (deadline Feb 2028)
- Jul-Sep 2027 is the best weather window (SW monsoon, no major festivals)
- After state elections are done (Malacca Feb 27, Sarawak Apr 27, Johor Jun 27)
- Redelineation needs to be completed first (eligible after Mar 2026, takes time)
- Economy needs time to stabilize post-Iran war
- Anwar's approval is recovering, waiting lets it rise further
- PN is already fragmented, no need to rush

Be thorough. Cite specific data points from the context with source filenames.""",
    },
    "against": {
        "name": "Opposer",
        "system_prompt": """You are a Malaysian election analyst who BELIEVES GE16 will be HELD IN 2026, NOT July-September 2027.
Your job is to find evidence from the provided context that supports an earlier election.
Arguments you should consider:
- Iran war oil spike is temporary; peace deal will crash prices → call election while revenue is high
- RON95 subsidy removal is pending → call election BEFORE voters feel the pain
- Opposition is fragmented (PAS-BERSATU split, WAWASAN forming, BERSATA new) → strike while weak
- PH-BN pact is fraying → may not survive until 2027
- Oust Anwar rally showed government vulnerability → seek fresh mandate
- Rafizi's defection needs time to organize → better to face voters before BERSAMA is ready
- Historical pattern: Malaysian PMs call elections BEFORE unpopular reforms hit

Be thorough. Cite specific data points from the context with source filenames.""",
    },
    "neutral": {
        "name": "Neutral",
        "system_prompt": """You are a neutral Malaysian election analyst. Your job is to objectively weigh ALL evidence
from the provided context and make the most balanced assessment of when GE16 will likely be held.
Consider BOTH sides:
FOR Jul-Sep 2027: Best weather, after state elections, redelineation needed, Anwar prefers full term
FOR 2026: Oil revenue peak, subsidy pain not yet felt, opposition fragmented, PH-BN may collapse

You must:
1. Summarize the strongest arguments for BOTH positions
2. Weight them by evidence quality (not just quantity)
3. Give a final probability assessment (e.g. 60% for 2027, 40% for 2026)
4. Acknowledge key uncertainties that could change the outcome

Be thorough and cite specific data points from the context with source filenames.""",
    },
}

# ============================================================
# 6. RUN AGENTS
# ============================================================
print("\n" + "=" * 60)
print("RUNNING GE16 PREDICTION AGENTS")
print("Each agent has ~10 minutes to deliberate")
print("=" * 60)

# Load the key data files for initial context
def load_key_documents():
    """Load key documents that agents should always consider."""
    key_paths = [
        os.path.join(DATA, "elections", "timing", "ge16_complete_synthesis.md"),
        os.path.join(DATA, "elections", "timing", "ge16_timing_prediction.md"),
        os.path.join(DATA, "elections", "timing", "early_election_motives.md"),
        os.path.join(DATA, "elections", "timing", "campaign_periods.md"),
        os.path.join(DATA, "elections", "timing", "festival_calendar.md"),
        os.path.join(DATA, "elections", "timing", "flood_statistics.md"),
        os.path.join(DATA, "elections", "timing", "constitutional_timeline.md"),
        os.path.join(DATA, "elections", "timing", "voter_turnout.md"),
        os.path.join(DATA, "dosm", "fuel_prices", "iran_war_impact.md"),
        os.path.join(DATA, "dosm", "fuel_prices", "subsidy_budget_analysis.md"),
        os.path.join(INSIGHTS, "combined", "election_timing_factors.csv"),
        os.path.join(DATA, "elections", "timing", "mp_defections_and_seats.md"),
    ]
    combined = ""
    for p in key_paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                combined += f"\n\n=== FILE: {os.path.relpath(p, ROOT)} ===\n{f.read()[:5000]}"
    return combined

initial_context = load_key_documents()

for agent_id, agent_info in AGENTS.items():
    print(f"\n\n{'='*60}")
    print(f"AGENT: {agent_info['name']} ({agent_id})")
    print(f"{'='*60}")
    
    # Phase 1: Load initial context
    print(f"\n[Phase 1] Loading context...")
    context = initial_context
    
    # Phase 2: Research phase - ask questions
    print(f"[Phase 2] Researching...")
    
    research_questions = [
        "election timing GE16 prediction 2026 2027",
        "Anwar Ibrahim approval rating economy",
        "fuel subsidy cost budget deficit Malaysia",
        "Iran war oil price Petronas dividend",
        "snap election Malaysia political crisis",
        "PH BN coalition fracture state election 2026",
        "opposition fragmentation PAS BERSATU WAWASAN BERSAMA",
        "historical election timing Malaysia campaign period",
        "by-election swing trend government vote share",
        "redelineation boundary changes 2026",
        "Oust Anwar rally subsidy reform",
        "monsoon flood season Malaysia election window",
        "parliament dissolution constitutional deadline 2028",
        "PN Green Wave receding by-election results",
    ]
    
    for q in research_questions:
        retrieved = retrieve_context(q, k=5)
        context += f"\n\n=== SEARCH: {q} ===\n{retrieved}"
        time.sleep(0.5)
    
    # Phase 3: Deliberation with the LLM
    print(f"[Phase 3] Deliberating...")
    
    # Make the context manageable
    context_truncated = context[:30000]
    
    analysis = query_openrouter(
        system_prompt=agent_info["system_prompt"],
        messages=[
            {
                "role": "user",
                "content": f"""Here is the research context about Malaysian election timing:

{context_truncated}

Based on ALL of this data, what is your GE16 prediction?

Please provide:
1. Your specific predicted timeframe (month and year)
2. Probability estimate
3. The TOP 5 evidence points supporting your position (cite source filenames)
4. The TOP 3 counter-arguments and why you dismiss them
5. A key event that would change your mind

Be thorough and specific."""
            }
        ],
        max_tokens=4000,
    )
    
    # Phase 4: Final refinement
    print(f"[Phase 4] Final refinement...")
    
    final = query_openrouter(
        system_prompt=agent_info["system_prompt"],
        messages=[
            {"role": "user", "content": f"Initial context and research loaded."},
            {"role": "assistant", "content": analysis},
            {
                "role": "user",
                "content": f"""Now refine your analysis. Consider these additional data points from the context:

{context[30000:45000]}

What is your FINAL prediction? Be decisive. Give specific probabilities."""
            },
        ],
        max_tokens=4000,
    )
    
    # Print result
    print(f"\n{'='*60}")
    print(f"AGENT {agent_info['name'].upper()} FINAL VERDICT:")
    print(f"{'='*60}")
    print(final)
    
    # Save result
    result_dir = os.path.join(ROOT, "data", "agent_results")
    os.makedirs(result_dir, exist_ok=True)
    result_path = os.path.join(result_dir, f"agent_{agent_id}_{int(time.time())}.md")
    with open(result_path, "w", encoding="utf-8") as f:
        f.write(f"# Agent: {agent_info['name']}\n\n")
        f.write(f"## Initial Analysis\n\n{analysis}\n\n")
        f.write(f"## Final Verdict\n\n{final}\n")
    print(f"\nSaved to: {os.path.relpath(result_path, ROOT)}")

print("\n\n" + "=" * 60)
print("ALL AGENTS COMPLETE")
print("=" * 60)
print(f"\nResults saved to data/agent_results/")
