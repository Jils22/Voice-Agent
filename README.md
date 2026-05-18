# 🎙️ SUVIT AI VOICE AGENT: Multilingual Real-Time AI Support Engine

SUVIT AI VOICE AGENT is a state-of-the-art, low-latency voice-to-voice orchestration engine designed for high-performance customer support environments. Built on a modular "Service-Engine" architecture, it delivers sub-2-second end-to-end response times with native support for English, Hindi (Hinglish), and Gujarati.

---

## 🏗️ Rebranded Architecture & Terminology

The system is organized into distinct functional domains for maximum maintainability. Here is a guide to the terminology used in this project:

| Engine Name | Legacy Term | Description |
| :--- | :--- | :--- |
| **`listener`** | STT | Real-time Speech-to-Text engine with speculative RAG triggering. |
| **`thinker`** | LLM | Conversational AI brain (GPT-4o-mini) and history management. |
| **`speaker`** | TTS | High-fidelity Voice Synthesis with 25ms linear smoothing. |
| **`library`** | RAG | Hybrid knowledge retrieval (Semantic + Keyword) with reranking. |
| **`orchestrator`** | Pipeline | The primary async workflow that manages turn-ownership and barge-in. |
| **`store`** | Database | Persistent storage for vector indices, metadata, and raw documentation. |
| **`ops`** | Scripts | Infrastructure tasks including scraping and index ingestion. |

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10+** (Recommend 3.13 for best performance)
- **Node.js 18+**
- **API Keys**: 
  - [Deepgram](https://console.deepgram.com/) (STT)
  - [OpenAI](https://platform.openai.com/) (LLM)
  - [Google Gemini](https://aistudio.google.com/) (Fallback LLM)
  - [Sarvam AI](https://www.sarvam.ai/) (Multilingual TTS)

---

## 🚀 Installation & Setup

### 1. Backend Configuration
Navigate to the backend directory and set up your environment:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` folder with the following keys:
```env
DEEPGRAM_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
SARVAMAI_API_KEY=your_key_here
```

### 2. Knowledge Base Initialization
To populate the AI's brain with your own documentation:
```powershell
# 1. Scrape data (defaults to Vyapar/TaxOne help center)
python -m ops.scraper

# 2. Build the search index
python -m ops.ingest
```

### 3. Launching the Engine
Start the FastAPI server:
```powershell
uvicorn app:app --reload --port 8000
```

### 4. Interface Deployment
The frontend is a dedicated React + Vite application featuring a premium animated UI, completely decoupled from backend rendering to ensure zero latency impact on the voice pipeline.
```powershell
cd ../frontend
npm install
npm run dev
# The frontend will run on http://localhost:3000 and automatically proxy WebSocket connections to the backend on port 8000.
```

---

## ✨ Recent Improvements (UI & VAD Upgrade)

- **Premium UI Aesthetics**: Introduced a dynamic, glassmorphism-inspired interface using Framer Motion. 
- **VoiceOrb Visualizer**: A highly responsive, GPU-accelerated animated orb that reacts logarithmically to microphone `vadEnergy` in real-time.
- **Strict Background Noise Rejection**: Upgraded the local `audioWorklet` VAD (`audio-processor.js`). The agent now demands a higher threshold of sustained vocal volume to be interrupted, completely ignoring background noise or typing.
- **Smart Endpointing**: Deepgram's silence timeout (`endpointing`) was increased from 300ms to 1000ms in `backend/listener/engine.py`. The agent now gracefully waits for you to finish your sentence instead of cutting you off when you take a breath.

---

## 🛡️ Verification & Testing
The system includes a suite of verification scripts to ensure each engine is performing optimally:
- `python verify_listener.py`: Validate real-time transcription and Deepgram connectivity.
- `python verify_brain.py`: Test LLM logic and context retrieval.
- `python verify_flow.py`: End-to-end pipeline verification (STT → LLM → TTS).

---

*SUVIT AI VOICE AGENT — Redefining Human-AI Conversation.*
