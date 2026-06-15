"""
Build reusable document index (TF-IDF based, no external API calls).
Run once: python scrape/build_vectorstore.py
"""

import os, sys, glob, json, pickle, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
INSIGHTS = os.path.join(ROOT, "insights")
INDEX_DIR = os.path.join(ROOT, "data", ".doc_index")
os.makedirs(INDEX_DIR, exist_ok=True)

def load_all_docs():
    docs = []
    
    # All .md files
    for fpath in glob.glob(os.path.join(DATA, "**", "*.md"), recursive=True):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if len(content.strip()) > 100:
                rel = os.path.relpath(fpath, ROOT)
                docs.append({"source": rel, "text": content})
        except:
            pass
    
    # CSV files
    for fpath in glob.glob(os.path.join(DATA, "**", "*.csv"), recursive=True):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if len(content.strip()) > 100:
                rel = os.path.relpath(fpath, ROOT)
                docs.append({"source": rel, "text": f"CSV DATA FROM {rel}:\n{content[:50000]}"})
        except:
            pass
    
    # Insights
    for fpath in glob.glob(os.path.join(INSIGHTS, "**", "*.md"), recursive=True):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if len(content.strip()) > 100:
                rel = os.path.relpath(fpath, ROOT)
                docs.append({"source": rel, "text": content})
        except:
            pass
    
    return docs

print("Loading documents...")
docs = load_all_docs()
print(f"Loaded {len(docs)} documents")

# Split into chunks
chunks = []
chunk_sources = []
for doc in docs:
    text = doc["text"]
    # Split by sections or paragraphs (~1500 char chunks)
    parts = re.split(r'\n#{1,3}\s+|\n---\n|\n\n', text)
    for part in parts:
        part = part.strip()
        if len(part) > 200:
            chunks.append(part[:3000])
            chunk_sources.append(doc["source"])

print(f"Created {len(chunks)} chunks")

# Build TF-IDF matrix
print("Building TF-IDF index...")
vectorizer = TfidfVectorizer(max_features=50000, stop_words="english", 
                             ngram_range=(1, 2), min_df=2)
tfidf_matrix = vectorizer.fit_transform(chunks)
print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")

# Save everything
with open(os.path.join(INDEX_DIR, "chunks.pkl"), "wb") as f:
    pickle.dump(chunks, f)
with open(os.path.join(INDEX_DIR, "sources.pkl"), "wb") as f:
    pickle.dump(chunk_sources, f)
with open(os.path.join(INDEX_DIR, "vectorizer.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)
with open(os.path.join(INDEX_DIR, "matrix.pkl"), "wb") as f:
    pickle.dump(tfidf_matrix, f)

print(f"\nIndex saved to {INDEX_DIR}")
print(f"Total chunks indexed: {len(chunks)}")
print("Ready for agent queries!")
