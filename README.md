# PromptPackr
**Compress your conversations. Reuse your prompts. Supercharge your agents.**  PromptPackr is a local, privacy-first tool that **compresses lengthy chat history into structured memory** — making it easier to reuse, audit, and rehydrate LLM prompts.   It's like creating `.zip` files for your AI conversations.

## ✨ Features
- 🔹 Generate **compressed summaries** of long conversations
- 🧾 Extract **key instructions and goals**
- 🎭 Detect **tone and communication style**
- 🧠 Enable **prompt rehydration** for autonomous agents or RAG pipelines
- 🔒 100% **offline** — no API keys or cloud calls

  ## 🛠 Built With
- 🦙 [Ollama](https://ollama.com/) — Local LLM runtime (e.g., Mistral, LLaMA 3)
- 🌐 [Streamlit](https://streamlit.io/) — Web-based UI
- 🐍 Python — Core compression logic

## 📸 Demo
<img width="298" alt="res1" src="https://github.com/user-attachments/assets/d790bcf7-92cc-4967-a939-81ba37d29db0" />

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/promptpackr.git
cd promptpackr
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Install and run Ollama
Download Ollama:
👉 https://ollama.com/download

Pull a model (e.g., Mistral):
```bash
ollama run mistral
```

4. Launch the app
```bash
streamlit run app.py
```

🧪 Sample Input
Just upload a .txt file of a multi-turn conversation:

📤 Output Format
🔹 Summary — High-level chat overview
🧾 Instructions — Clear, bullet-pointed tasks
🎭 Tone — Communication style (e.g., friendly, formal)

All output is returned in structured format and can optionally be exported or rehydrated into a new prompt.

📦 Folder Structure
```bash
promptpackr/
├── app.py                # Streamlit interface
├── ollama_query.py       # LLM interaction logic
├── prompts.py            # Prompt templates
├── sample_chat.txt       # Sample input
├── requirements.txt
└── README.md
```
🧠 Use Cases
✍️ Improve prompt reusability
🤖 Store long LLM conversations in compressed form
💬 Build memory-aware agents
🧪 Analyze support logs or meeting transcripts

🔐 Local-Only Architecture
No API keys. No cloud servers.
PromptPackr runs 100% locally using Ollama + open-source LLMs.

.

📬 Contributing
Have a feature idea? Want to add Chainlit or memory export?
Pull requests are welcome! You can also open an issue for feedback or improvements.

🔗 Connect
Built with Varshitha Yanamala during #30DaysOfGenAI






