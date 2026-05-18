import os
import ssl
import sys

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

print("\n" + "="*50)
print("🚀 SUVIT AI VOICE AGENT - MODEL WARMUP")
print("="*50)
print("Downloading 'The Brain' models (approx 1.5GB total).")
print("This only happens once. Please wait for the progress bars...\n")

try:
    from langchain_huggingface import HuggingFaceEmbeddings
    from sentence_transformers import CrossEncoder
    from settings import EMBEDDING_MODEL, RERANKER_MODEL

    print(f"📦 Step 1/2: Loading Embedding Model ({EMBEDDING_MODEL})...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    print("✅ Embedding Model Ready.\n")

    print(f"📦 Step 2/2: Loading Reranker Model ({RERANKER_MODEL})...")
    reranker = CrossEncoder(RERANKER_MODEL)
    print("✅ Reranker Model Ready.\n")

    print("="*50)
    print("🎉 ALL MODELS DOWNLOADED SUCCESSFULLY!")
    print("You can now run: uvicorn app:app --reload")
    print("="*50 + "\n")

except Exception as e:
    print(f"\n❌ ERROR DURING WARMUP: {e}")
    print("Please check your internet connection and try again.")
