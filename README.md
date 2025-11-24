# EnterpriseAssist AI — Multi-Agent Customer Support System  
### Kaggle 5-Day AI Agents Intensive Capstone Project  
**Track:** Enterprise Agents  
**Author:** Vineet Khatri  

---

## 🧩 Project Overview  
EnterpriseAssist AI is a multi-agent customer support automation system designed using the concepts learned during the *5-Day AI Agents Intensive Course by Google & Kaggle*.  
The system automates common enterprise support tasks, including:

- Intent detection  
- Knowledge base lookup  
- Troubleshooting  
- Ticket creation  
- Multi-step routing  
- Agent collaboration  
- Logging & evaluation  

This solution demonstrates real-world enterprise workflows powered by LLM agents and ADK-style design.

---

## 🏗️ Architecture

The system contains **four coordinated agents** working together:

### **1. IntakeAgent**  
Identifies user intent  
Routes message to the appropriate workflow  
Extracts structured data

### **2. SupportAgent**  
Uses KB Lookup Tool  
Generates helpful troubleshooting steps  
Responds to user queries

### **3. EscalationAgent**  
Uses Diagnostics Tool  
Creates support tickets when needed  
Handles unresolved issues

### **4. OrchestratorAgent**  
Controls workflow  
Calls the right agent at the right time  
Logs all events into `logs.json`

---

## 🧰 Tools Used  
- `search_stub_tool.py`  
- `knowledge_base_tool.py`  
- `diagnostics_tool.py`  
- `ticket_api_tool.py`  

All tools follow the ADK-style interface.

---

## 🧠 Memory System  
- **Session Memory** for short-term context  
- **Long-Term Memory (MemoryBank)** for storing resolved issues  

---

## 📊 Observability  
- All events saved to `logs.json`  
- Includes: timestamps, intents, agent actions, metrics  

---

## 🧪 Example Run  

```bash
python main.py
```

Output:

```json
{
  "action": "respond",
  "text": "Based on user message: I need a refund",
  "tool": null
}
```

Logs appear in:  
```
logs.json
```

---

## 🚀 Installation & Setup  

### Clone the repository
```bash
git clone https://github.com/<your-username>/EnterpriseAssistAI.git
cd EnterpriseAssistAI
```

### Run the project  
```bash
python main.py
```

No external API keys needed.  
No billing required.

---

## 📁 Folder Structure  

```
src/
 ├── agents/
 │   ├── intake_agent.py
 │   ├── support_agent.py
 │   ├── escalation_agent.py
 │   └── orchestrator.py
 ├── tools/
 │   ├── search_stub_tool.py
 │   ├── knowledge_base_tool.py
 │   ├── diagnostics_tool.py
 │   └── ticket_api_tool.py
 ├── memory/
 │   ├── session_manager.py
 │   └── long_term_memory.py
 ├── eval/
 │   ├── evaluator.py
 │   └── judge.py
 ├── observability/
 │   ├── logger.py
 │   └── metrics.py
logs.json  
main.py
```

---

## 🎥 (Optional) Demo Video  
Not required for submission.  
If added, place the link here.

---

## 🏆 Kaggle Capstone Submission  
This GitHub repository is attached as part of my submission for the **Enterprise Agents Track**.

---

## 📜 License  
MIT License  
