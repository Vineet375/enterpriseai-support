# memory.py - simple session + long-term memory (simulated)
import json
from typing import Dict, Any, List
from collections import defaultdict

class SessionStore:
    def __init__(self):
        self.sessions = {}  # session_id -> list(messages)
    def create(self, session_id: str):
        self.sessions[session_id] = []
    def append(self, session_id: str, msg: Dict[str,Any]):
        self.sessions.setdefault(session_id, []).append(msg)
    def get(self, session_id: str):
        return self.sessions.get(session_id, [])

class LongTermMemory:
    def __init__(self):
        self.memory = []  # list of (emb, text, meta)
    def add(self, text: str, meta: Dict[str,Any]):
        # simple append: for demo we don't compute embeddings
        self.memory.append({"text":text,"meta":meta})
    def query(self, hint: str, k=3):
        # naive scoring by keyword overlap
        hits = []
        for m in self.memory:
            score = sum(1 for tok in hint.lower().split() if tok in m["text"].lower())
            if score>0:
                hits.append((score,m))
        hits = sorted(hits, key=lambda x:-x[0])
        return [h[1] for h in hits[:k]]
