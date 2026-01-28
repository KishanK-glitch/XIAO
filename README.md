# XIAO: Context-Aware LLM Backend

**XIAO** is a high-performance, asynchronous AI backend engineered to deliver context-aware responses using the Groq inference engine. It uses a Retrieval-Augmented Generation (RAG) approach by injecting structured user context directly into the system prompt, ensuring the AI "knows" the user's engineering background, projects, and preferences without needing fine-tuning.

---

## ⚡ Key Features

* **FastAPI Powered:** Built on a modern, non-blocking asynchronous web framework for high throughput.
* **Groq LPU Integration:** Leverages the Groq API for near-instantaneous inference speeds with Llama 3 / Mixtral models.
* **Dynamic Context Injection:** Automatically loads user profiles (`data.json`) to personalize every interaction.
* **Clean Architecture:** Implements a strict Service-Repository pattern with separation of concerns (Core Logic vs. API Services).
* **Type Safety:** Uses **Pydantic** for rigorous data validation on both input and output.

---

## 🛠️ Technical Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI)
* **LLM Provider:** Groq Cloud
* **Configuration:** Pydantic Settings & Dotenv

---

## 📂 Project Structure

The project follows a production-grade modular hierarchy:

```text
XIAO/
├── app/
│   ├── __init__.py
│   ├── main.py       # Application Entry Point & Routes
│   ├── services.py   # External API Client (Groq Integration)
│   ├── core.py       # Context Loading & System Prompt Logic
│   ├── models.py     # Pydantic Data Schemas
│   └── config.py     # Environment Variable Management
├── data.json         # User Knowledge Base (Context Source)
├── .env              # Secrets & API Keys (Excluded from Git)
├── requirements.txt  # Project Dependencies
└── README.md         # Documentation