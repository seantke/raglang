# Raglang

## ✅ Phase 1: Sentence Breakdown MVP (English → Korean)

> 🔧 Goal: Translate an English sentence, tokenize both sides, tag POS/morphology, and align word pairs in a UI.

* [ ] **Scaffold local project folder**

  * [ ] Create virtual environment
  * [ ] Create `src/`, `frontend/`, `models/`, `data/`, `scripts/` folders
  * [ ] Set up Poetry or `requirements.txt`

* [ ] **Backend API using FastAPI**

  * [ ] `/translate`: returns Korean sentence
  * [ ] `/analyze`: returns tokenized + POS-tagged breakdown of both English and Korean
  * [ ] `/align`: returns token alignment
  * [ ] `/full_breakdown`: returns structured JSON for full UI display

* [ ] **Frontend UI using Open WebUI or custom HTML/JS**

  * [ ] Sentence input (English)
  * [ ] Output table: side-by-side English and Korean tokens
  * [ ] Visual link arrows between English and Korean tokens

* [ ] **Translation model**

  * [ ] ✅ `facebook/nllb-200-distilled-600M` — multilingual, small

    * Memory: \~2.5 GB VRAM, \~5–6 GB RAM
  * [ ] OR `Helsinki-NLP/opus-mt-en-ko` — faster, smaller

    * Memory: \~1–2 GB RAM

* [ ] **Tokenization + POS tagging**

  * [ ] English: spaCy `en_core_web_sm`
  * [ ] Korean: KoNLPy + `Okt` or `Mecab`

    * Optional: `khaiii` or `stanza` for richer morphology (RAM: 1–2 GB)

* [ ] **Word alignment**

  * [ ] Use `awesome-align` or heuristics with attention matrix

    * Optional: Fine-tune later if needed

---

## ✅ Phase 2: Add Local Vector Store (ChromaDB)

> 🧠 Goal: Store translated/analyzed sentences + embeddings locally for RAG search

* [ ] Set up ChromaDB

  * [ ] Use persistent local DB mode (not in-memory)
  * [ ] Define schema: sentence, lang, tokens, POS tags, timestamp, embedding

* [ ] Embed sentences using:

  * ✅ `intfloat/multilingual-e5-large-instruct` (best multilingual embedding model as of 2025)

    * Memory: 7–8 GB RAM, \~4 GB VRAM for GPU inference (or 12+ GB RAM CPU)
    * [ ] Sentence-level embedding
    * [ ] Optionally: embed tokens for fine-grained retrieval

* [ ] Store all sentences + metadata in Chroma:

  * [ ] English sentence
  * [ ] Korean sentence
  * [ ] Token breakdowns
  * [ ] POS/morph/mapping
  * [ ] Embedding

* [ ] Implement `/store` and `/query` endpoints

* [ ] UI: Add history sidebar or recall search bar

---

## ✅ Phase 3: Add Local LLM for Context-Aware Tutor (RAG)

> 🧠 Goal: Ask questions like “Why is this verb conjugated?” or “What’s another way to say this?”

* [ ] Choose and run a **local LLM**:

  * ✅ `mistral-7b-instruct.Q4_K_M.gguf` (Good quality, 4-bit quant)

    * Memory: \~6–8 GB RAM (CPU) or \~4.5–6 GB VRAM (GPU)
  * Alternative: `phi-2` or `tinyllama` (2–4 GB RAM)

* [ ] Use `llama-cpp-python` or `llm` (from Open WebUI) backend

  * [ ] Load with context window > 4k if possible

* [ ] Add retrieval-augmented generation (RAG):

  * [ ] Query ChromaDB for similar past sentences
  * [ ] Inject relevant results into prompt for local LLM
  * [ ] Create `/tutor` endpoint (POST: question + context)

* [ ] UI: Add chat sidebar for grammar/tutor questions

---

## ✅ Phase 4: Active Recall and Quiz Features

> 🎓 Goal: Let users practice and recall previous sentences, especially weak areas

* [ ] Track usage / timestamps on sentence entries

* [ ] Implement spaced repetition scheduling (Leitner-like logic)

* [ ] Create endpoints:

  * [ ] `/quiz/gap-fill`
  * [ ] `/quiz/translate`
  * [ ] `/quiz/conjugate`
  * [ ] `/quiz/order` (scrambled word ordering)

* [ ] UI: Add quiz mode toggle + options

---

## ✅ Phase 5: Speech and Audio Add-on (Optional)

> 🔊 Goal: Enable listening + speaking support using local audio models

* [ ] Add speech input:

  * ✅ `whisper.cpp` or `faster-whisper`

    * RAM: 2–3 GB (`base`), 4–6 GB (`medium`)
  * [ ] Endpoint: `/transcribe`

* [ ] Add speech output:

  * [ ] Use `TTS` models like `coqui-ai/TTS`, `piper`, or `OpenTTS`

    * Korean TTS models available in `piper`

* [ ] UI:

  * [ ] Add audio record + playback buttons
  * [ ] Optionally show waveform or pronunciation feedback

---

## ✅ Optional Phase 6: Visual Grammar and Flow Charts

> 🎨 Goal: Visualize sentence structure or grammar as trees/flows

* [ ] Generate tree from POS data
* [ ] Render as SVG using D3.js or simple canvas
* [ ] Link to sentence in vector DB

---

## 🧰 Total Model Memory Overview

| Model / Tool                      | Task                 | RAM (CPU)  | VRAM (GPU) |
| --------------------------------- | -------------------- | ---------- | ---------- |
| `nllb-200-distilled-600M`         | Translation (en↔ko)  | \~6 GB     | \~2.5–3 GB |
| `opus-mt-en-ko`                   | Translation (faster) | \~2 GB     | \~1.5 GB   |
| `multilingual-e5-large-instruct`  | Embeddings           | \~8 GB     | \~4 GB     |
| `mistral-7b-instruct.Q4_K_M.gguf` | RAG LLM              | \~7–8 GB   | \~6 GB     |
| `phi-2`                           | LLM (small)          | \~3–4 GB   | \~2–3 GB   |
| `whisper.cpp (base)`              | Speech recognition   | \~2 GB     | \~1.5 GB   |
| `piper`                           | TTS                  | \~0.5–1 GB | \~0.5–1 GB |
| KoNLPy + Okt                      | Korean NLP           | \~1 GB     | N/A        |
| `awesome-align`                   | Token alignment      | \~2–3 GB   | N/A        |
| ChromaDB                          | Vector DB            | \~1 GB     | N/A        |
