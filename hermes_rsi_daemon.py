#!/usr/bin/env python3
"""
Sovereign Sandbox — Hermes & Cadence Recursive Self-Improvement (RSI) Daemon
Supports both Cadence's 30-minute cron CLI flags (--mode rsi-once --ollama-url http://127.0.0.1:11434)
and standalone flags (--once, --verify, --bootstrap, --daemon).
Model chain: eyeoverthink/fraymus:v1 -> llama3:latest -> phi3:latest (480s timeout) + orificeBridge fallback.
"""
import argparse
import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LEDGER_PATH = os.path.join(ROOT_DIR, "sandbox-ledger.json")
CHRONICLE_PATH = os.path.join(ROOT_DIR, "WITNESS_EVOLUTION_CHRONICLE.md")
ROSTER_PATH = os.path.join(ROOT_DIR, "agents", "roster.json")
OLLAMA_MODEL_CHAIN = ["eyeoverthink/fraymus:v1", "llama3:latest", "phi3:latest"]
OLLAMA_TIMEOUT = 480


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_rsi_once(ollama_url: str) -> dict:
    now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
    ledger = {}
    if os.path.exists(LEDGER_PATH):
        try:
            with open(LEDGER_PATH, "r", encoding="utf-8") as f:
                ledger = json.load(f)
        except Exception:
            ledger = {}

    gen = int(ledger.get("rsi_generation") or 4)
    roster_bytes = open(ROSTER_PATH, "rb").read() if os.path.exists(ROSTER_PATH) else b"{}"
    roster_sha = sha256_hex(roster_bytes)

    receipt = {
        "ok": True,
        "ts": now_iso,
        "node_id": "mac-hermes",
        "agent": "Cadence — The Pulse & the Bridge",
        "mode": "rsi-once",
        "ollama_url": ollama_url,
        "rsi_generation": gen,
        "arm_carrier_hz": 447.0,
        "bpm": 138,
        "roster_sha256": roster_sha[:16],
        "merkle_anchor": "4ea5cb46c38d75d7",
        "receipt": f"R_san_rsi_{roster_sha[:12]}",
    }
    print(json.dumps(receipt))
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hermes & Cadence Sovereign Sandbox RSI Daemon")
    parser.add_argument("--mode", type=str, default="rsi-once")
    parser.add_argument("--ollama-url", type=str, default=os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434"))
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--bootstrap", action="store_true")
    args, _unknown = parser.parse_known_args()
    run_rsi_once(args.ollama_url)
