# agents.py - simple Agent classes (orchestrator + specialists)
from typing import Dict, Any
from src.tools import kb_lookup, search_stub, ticket_api_create, diagnostic_executor
from src.memory import SessionStore, LongTermMemory

session_store = SessionStore()
lt_memory = LongTermMemory()

class BaseAgent:
    def __init__(self, name):
        self.name = name
    def act(self, user_msg: str, context: Dict[str,Any]) -> Dict[str,Any]:
        raise NotImplementedError

class TriageAgent(BaseAgent):
    def act(self, user_msg: str, context: Dict[str,Any]):
        # naive triage: route by keywords
        if "bill" in user_msg.lower() or "refund" in user_msg.lower():
            return {"action":"route","target":"billing","reason":"billing keywords"}
        if "error" in user_msg.lower() or "not working" in user_msg.lower():
            return {"action":"route","target":"diagnostics","reason":"error keywords"}
        return {"action":"route","target":"billing","reason":"default"}

class BillingAgent(BaseAgent):
    def act(self, user_msg: str, context: Dict[str,Any]):
        # try KB
        kb = kb_lookup(user_msg)
        if "No exact" not in kb["result"]:
            return {"action":"respond","text":kb["result"],"tool_result":kb}
        # fallback to search
        s = search_stub(user_msg)
        return {"action":"respond","text":s["results"][0]["snippet"],"tool_result":s}

class DiagnosticsAgent(BaseAgent):
    def act(self, user_msg: str, context: Dict[str,Any]):
        # run diagnostics if asked
        if "diagnose" in user_msg.lower() or "run" in user_msg.lower():
            r = diagnostic_executor("run")
            return {"action":"respond","text":r["output"],"tool_result":r}
        # else escalate / create ticket
        ticket = ticket_api_create(context.get("customer_id","unknown"), user_msg)
        return {"action":"respond","text":f"Created a ticket: {ticket['ticket_id']}", "ticket":ticket}
