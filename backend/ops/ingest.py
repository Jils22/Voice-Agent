import os
import glob
import pickle
import re
# ULTIMATE SSL OVERRIDE (Final Boss Patch)
def apply_ultimate_ssl_patch():
    import ssl
    try:
        orig_create_default_context = ssl.create_default_context
        def patched_create_default_context(*args, **kwargs):
            context = orig_create_default_context(*args, **kwargs)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            return context
        ssl.create_default_context = patched_create_default_context
        ssl._create_default_https_context = ssl._create_unverified_context
        
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        orig_init = urllib3.connectionpool.HTTPConnectionPool.__init__
        def new_init(self, *args, **kwargs):
            kwargs['cert_reqs'] = 'CERT_NONE'
            kwargs['assert_hostname'] = False
            return orig_init(self, *args, **kwargs)
        urllib3.connectionpool.HTTPConnectionPool.__init__ = new_init
    except: pass

apply_ultimate_ssl_patch()

os.environ["CURL_CA_BUNDLE"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"
os.environ["HF_HUB_DISABLE_SSL_VERIFY"] = "1"
os.environ["GIT_SSL_NO_VERIFY"] = "true"

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "store", "docs")
INDEX_DIR = os.path.join(os.path.dirname(__file__), "..", "store", "index")

def ingest():
    md_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    if not md_files:
        print(f"No .md files found in {DOCS_DIR}")
        print(f"Put your .md files in: {DOCS_DIR}")
        return

    raw_docs = []
    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            # CLEANING: Remove navigation bars, footers, and redundant links (Principle: Clean Context)
            content = re.sub(r'\[.*?\]\(.*?\)', '', content) # Remove markdown links
            content = re.sub(r'http\S+', '', content)       # Remove URLs
            content = re.sub(r'Navigation|Menu|Footer|All Collections|Frequently Asked Question', '', content, flags=re.I)
            content = re.sub(r'\n{3,}', '\n\n', content)     # Remove excessive newlines
            
            raw_docs.append(Document(page_content=content, metadata={"source": path}))
        print(f"Loaded and Cleaned: {path}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
    chunks = splitter.split_documents(raw_docs)
    print(f"Created {len(chunks)} chunks from {len(md_files)} files")

    print("Loading embedding model (first run downloads ~90MB)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        model_kwargs={"local_files_only": False}
    )

    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_DIR)
    
    print("Saving chunks for BM25...")
    import pickle
    with open(os.path.join(INDEX_DIR, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)
        
    print(f"Done. Index and chunks saved to {INDEX_DIR}")

if __name__ == "__main__":
    ingest()