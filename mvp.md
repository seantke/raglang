# 🧭 Suggested Roadmap (Minimal Viable Path for Local Learning)

---

## 🔹 Phase 1: Proof of Concept (No Translation Yet)

* [ ] Simple UI (Open WebUI or Streamlit/Gradio)
* [ ] Input: English sentence
* [ ] Output:

  * POS tagging (spaCy or stanza)
  * Word-by-word breakdown
  * Embeddings using `intfloat/e5-small` (multilingual-capable)
* [ ] Store tagged info + embeddings in ChromaDB

👉 **Goal:** prove you can break down language and build a memory structure for it.

---

## 🔹 Phase 2: Add Translation (One Language Pair Only)

* [ ] Integrate `facebook/nllb-200-distilled-600M` or `argos-translate` for English → Korean
* [ ] Align English ↔ Korean tokens using `awesome-align` (precomputed)
* [ ] Show word-by-word breakdowns and alignment links

👉 **Goal:** show that you can link and store bilingual sentence breakdowns with grammatical tags and embeddings.

---

## 🔹 Phase 3: Enrich + Optimize

* [ ] Add POS tagging for Korean (e.g. `stanza`, `KoNLPy`, or multilingual spaCy)
* [ ] Optimize memory (lazy loading, caching, DuckDB for persistent structure)
* [ ] Refactor components into backend (FastAPI or Flask API)

👉 **Goal:** reach a polished demo that can teach you something *yourself* and serve as a starting point for others.

---

## 🔹 Phase 4: Learning Loop / RAG Tool

* [ ] Design notebook-style “language journal” interface
* [ ] Add ability to recall similar sentences using vector search
* [ ] Highlight new vocabulary, irregular grammar, and reuse of known patterns
* [ ] Bonus: text-to-speech (Korean) using Coqui-TTS

👉 **Goal:** begin forming a real-time feedback + memory loop for long-term language learning.

---

## 🔄 What You Can Keep Iterating On

* Replace core models later (better translators, better embeddings)
* Expand to speech (whisper, TTS)
* Add more languages (NLLB makes it easy)
* Add gamification, spaced repetition, goal tracking

---

## 🛠️ Tooling That Balances Power + Simplicity

| Purpose         | Recommended Tool                                                 | Notes                                                 |
| --------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| UI              | [Open WebUI](https://github.com/open-webui/open-webui) or Gradio | Simple frontend                                       |
| POS Tagging     | spaCy / stanza                                                   | spaCy is faster, stanza is more accurate multilingual |
| Embeddings      | `intfloat/multilingual-e5-small`                                 | 400MB RAM, good for learning and scalable later       |
| Translation     | NLLB-200 distilled                                               | 1.5GB RAM, supports 200+ languages                    |
| Token Alignment | `awesome-align`                                                  | Run once per sentence pair and cache                  |
| Vector DB       | Chroma or DuckDB                                                 | Easy, local-first                                     |
| Memory/Notes DB | SQLite or TinyDB                                                 | Optional, for building user journal                   |
| Backend         | FastAPI                                                          | Clean API layer when you outgrow notebooks            |

---

## 💡 Bonus Tip: Document From Day 1

Even if you don’t publish right away:

* Keep **logs** of issues, model comparisons, memory use, results
* Save **screenshots** of UI iterations and design diagrams
* Write small weekly summaries (“What I tried / What worked / What didn’t”)

This will **dramatically improve** your ability to eventually turn this into:

* A blog series
* A product pitch
* A GitHub case study
