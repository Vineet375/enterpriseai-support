# tools.py -- simple tool wrappers (simulated)
import time
import json
from typing import Dict, Any

# Simple KB lookup (local JSON)
KB = {
    "billing/refund_policy": "Refunds processed within 7 business days. Contact billing@company.com.",
    "account/password_reset": "To reset your password, click 'Forgot password' and follow steps sent to your email."
}

def kb_lookup(query: str) -> Dict[str,Any]:
    # naive matching (demo)
    for k,v in KB.items():
        if any(tok in query.lower() for tok in k.split('/')):
            return {"tool":"kb_lookup","result":v}
    # fallback
    return {"tool":"kb_lookup","result":"No exact KB article found. Suggest escalation or search."}

def search_stub(query: str) -> Dict[str,Any]:
    # simulated web search
    snippets = [
        {"title":"Support - FAQ","snippet":"This page explains refund policies..."},
        {"title":"Forum - How to reset password","snippet":"Try clearing cookies and using password reset link."}
    ]
    time.sleep(0.5)
    return {"tool":"search","results":snippets}

def ticket_api_create(customer_id: str, issue: str) -> Dict[str,Any]:
    # simulate ticket creation
    ticket_id = f"TICKET-{int(time.time())%100000}"
    return {"tool":"ticket_api","ticket_id":ticket_id,"status":"created"}

def diagnostic_executor(code_snippet: str) -> Dict[str,Any]:
    # simulate running code - DO NOT execute arbitrary code in production
    return {"tool":"executor","output":"Diagnostics run complete: logs attached."}
