import os
import ssl
# Bypass SSL for model downloads
ssl._create_default_https_context = ssl._create_unverified_context
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["HF_HUB_DISABLE_SSL_VERIFY"] = "1"
import pickle
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from sentence_transformers import CrossEncoder

# Handle different LangChain version import patterns with extreme safety
try:
    from langchain_classic.retrievers import EnsembleRetriever
    from langchain_community.retrievers.bm25 import BM25Retriever
except ImportError:
    try:
        from langchain.retrievers import EnsembleRetriever
        from langchain_community.retrievers import BM25Retriever
    except ImportError:
        try:
            from langchain_community.retrievers import EnsembleRetriever, BM25Retriever
        except ImportError:
            EnsembleRetriever = None
            BM25Retriever = None
            print("[RAG] WARNING: Retrievers not found. Basic search only.")

from settings import INDEX_DIR, EMBEDDING_MODEL, RERANKER_MODEL

_ensemble_retriever = None
_reranker = None

def get_retriever():
    global _ensemble_retriever
    if _ensemble_retriever is None:
        print("[RAG] Loading hybrid search engine...")
        
        # 1. Load FAISS (Semantic Search)
        try:
            embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={"local_files_only": True} # FORCE LOCAL
            )
            
            if os.path.exists(os.path.join(INDEX_DIR, "index.faiss")):
                vs = FAISS.load_local(
                    INDEX_DIR, embeddings, allow_dangerous_deserialization=True
                )
                faiss_retriever = vs.as_retriever(search_kwargs={"k": 10})
            else:
                print(f"[RAG WARNING] FAISS index not found at {INDEX_DIR}")
                faiss_retriever = None
        except Exception as e:
            print(f"[RAG ERROR] Semantic model failed to load: {e}. Falling back to Keyword Search only.")
            faiss_retriever = None

        # 2. Load BM25 (Keyword Search)
        chunks_path = os.path.join(INDEX_DIR, "chunks.pkl")
        if os.path.exists(chunks_path) and BM25Retriever:
            try:
                with open(chunks_path, "rb") as f:
                    chunks = pickle.load(f)
                bm25_retriever = BM25Retriever.from_documents(chunks)
                bm25_retriever.k = 10
            except Exception as e:
                print(f"[RAG ERROR] BM25 failed: {e}")
                bm25_retriever = None
            
            # 3. Ensemble (Hybrid)
            if EnsembleRetriever and faiss_retriever and bm25_retriever:
                _ensemble_retriever = EnsembleRetriever(
                    retrievers=[bm25_retriever, faiss_retriever],
                    weights=[0.3, 0.7] # Semantic preferred, keywords catch exact terms
                )
                print("[RAG] Hybrid search active.")
            elif bm25_retriever:
                print("[RAG] Using BM25 (Keyword) only.")
                _ensemble_retriever = bm25_retriever
            elif faiss_retriever:
                print("[RAG] Using FAISS (Semantic) only.")
                _ensemble_retriever = faiss_retriever
            else:
                print("[RAG] No retrievers available!")
                _ensemble_retriever = None
        else:
            print("[RAG] chunks.pkl missing or BM25 disabled.")
            _ensemble_retriever = faiss_retriever
            
    return _ensemble_retriever

def get_reranker():
    global _reranker
    if _reranker is None:
        print("[RAG] Loading reranker (Offline)...")
        # Optimization: use local files only to avoid hub checks
        _reranker = CrossEncoder(RERANKER_MODEL, local_files_only=True)
    return _reranker

def retrieve(query: str, k: int = 5) -> list[str]:
    """Hybrid retrieval (FAISS + BM25) followed by Cross-Encoder reranking."""
    import traceback
    print(f"[RAG] Query: {query}")
    
    try:
        retriever = get_retriever()
        if retriever is None:
            print("[RAG ERROR] Retriever is None — index may not have been loaded. Returning empty.")
            return []

        # Get more candidates than k for reranking
        docs = retriever.invoke(query)
        print(f"[RAG] Raw docs returned: {len(docs) if docs else 0}")
        
        if not docs:
            print("[RAG WARNING] Retriever returned 0 docs for query.")
            return []

        # Deduplicate candidates
        seen = set()
        candidates = []
        for d in docs:
            content = d.page_content.strip()
            if content and content not in seen:
                candidates.append(content)
                seen.add(content)

        print(f"[RAG] Unique candidates after dedup: {len(candidates)}")

        # Reranking
        if len(candidates) > 1:
            reranker = get_reranker()
            pairs = [[query, c] for c in candidates]
            scores = reranker.predict(pairs)
            
            # Sort by score
            ranked_indices = np.argsort(scores)[::-1]
            results = [candidates[i] for i in ranked_indices[:k]]
            print(f"[RAG] Reranked {len(candidates)} candidates down to {len(results)}")
            return results
        
        return candidates[:k]

    except Exception as e:
        print(f"[RAG CRITICAL ERROR] retrieve() failed: {e}")
        traceback.print_exc()
        return []
