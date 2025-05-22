import os
import spacy
import torch
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
from chromadb import Client as ChromaClient
from chromadb.config import Settings
from deep_translator import GoogleTranslator
from rich import print
from uuid import uuid4

# ─── Load Models ───────────────────────────────────────────────────────────────
print("[bold cyan]Loading models...[/bold cyan]")

# POS tagger for English
nlp = spacy.load("en_core_web_sm")

# Multilingual E5-small embedding model (400MB, efficient)
embed_model = SentenceTransformer("intfloat/multilingual-e5-small")

# Simple translator: can switch to NLLB later for full local
translator = GoogleTranslator(source="en", target="ko")

# ─── Set Up Vector DB ──────────────────────────────────────────────────────────
print("[bold cyan]Setting up ChromaDB...[/bold cyan]")
chroma = ChromaClient(Settings(anonymized_telemetry=False))
if "lang-memory" not in [c.name for c in chroma.list_collections()]:
    db = chroma.create_collection("lang-memory")
else:
    db = chroma.get_collection("lang-memory")

# ─── Core Functionality ────────────────────────────────────────────────────────

def breakdown_english(text: str):
    doc = nlp(text)
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "pos": token.pos_,
            "lemma": token.lemma_,
            "tag": token.tag_,
        })
    return tokens

def embed_text(text: str):
    input_text = f"query: {text}"
    return embed_model.encode(input_text)

def store_sentence(original: str, translation: str, embedding):
    uid = str(uuid4())
    db.add(
        ids=[uid],
        documents=[original],
        metadatas=[{"translation": translation}],
        embeddings=[embedding.tolist()]
    )
    return uid

def simple_align(tokens_en, tokens_ko):
    # Placeholder alignment — can use awesome-align later
    return list(zip(tokens_en, tokens_ko))

def process(text: str):
    print(f"\n[bold yellow]Input:[/bold yellow] {text}")

    # POS Tagging
    en_tokens = breakdown_english(text)
    print("[bold green]English Tokens:[/bold green]")
    for t in en_tokens:
        print(f"  • {t['text']} ({t['pos']})")

    # Translation
    translation = translator.translate(text)
    print(f"\n[bold blue]Translation (Korean):[/bold blue] {translation}")

    # Naive token split
    ko_tokens = translation.split()  # Replace with real Korean tokenization later

    # Embedding & Storage
    embedding = embed_text(text)
    doc_id = store_sentence(text, translation, embedding)

    # Alignment (placeholder)
    aligned = simple_align([t["text"] for t in en_tokens], ko_tokens)
    print("\n[bold magenta]Naive Alignment:[/bold magenta]")
    for en, ko in aligned:
        print(f"  {en} ↔ {ko}")

    print(f"\n[dim]Stored as ID: {doc_id}[/dim]")

# ─── Main Loop ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("[bold]Language Learning Assistant[/bold]\n")
    while True:
        try:
            sentence = input("\nEnter an English sentence (or 'q' to quit):\n> ").strip()
            if sentence.lower() in {"q", "quit", "exit"}:
                break
            process(sentence)
        except KeyboardInterrupt:
            break
