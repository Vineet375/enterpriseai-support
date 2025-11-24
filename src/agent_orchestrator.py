# agent_orchestrator.py - orchestrates flow and logs
from src.agents import TriageAgent, BillingAgent, DiagnosticsAgent, session_store, lt_memory
import json, time

class Orchestrator:
    def __init__(self):
        self.triage = TriageAgent("triage")
        self.billing = BillingAgent("billing")
        self.diag = DiagnosticsAgent("diagnostics")
        self.logs = []

    def handle(self, session_id: str, user_msg: str, customer_id:str=None):
        # start session if not exists
        if session_id not in session_store.sessions:
            session_store.create(session_id)
        session_store.append(session_id, {"role":"user","text":user_msg,"ts":time.time()})
        context = {"customer_id":customer_id}

        # triage
        tri = self.triage.act(user_msg, context)
        self.logs.append({"step":"triage","result":tri})
        target = tri["target"]
        if target=="billing":
            res = self.billing.act(user_msg, context)
        else:
            res = self.diag.act(user_msg, context)
        self.logs.append({"step":"agent_response","agent":target,"result":res})
        # store memory if contains persistent info
        if "ticket" in res:
            lt_memory.add(f"ticket:{res['ticket']['ticket_id']}", {"session":session_id})
        return res

    def get_logs(self):
        return self.logs
