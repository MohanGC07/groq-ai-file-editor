# 🤖 Groq AI File Editor Agent

> An AI-powered file editing assistant built with Groq LLMs and Streamlit — enabling secure, natural language-driven file modifications with a sandboxed, tool-based agent architecture.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-red?logo=streamlit)](https://groq-ai-file-editor.streamlit.app/)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Security](#-security)
- [Project Structure](#-project-structure)
- [Local Setup](#-local-setup)
- [Deployment](#-deployment-streamlit-cloud)
- [Example Instructions](#-example-instructions)
- [Limitations](#-limitations)
- [Roadmap](#-roadmap)
- [Learning Outcomes](#-learning-outcomes)
- [License](#-license)
- [Author](#-author)

---

## 🧠 Overview

The **Groq AI File Editor Agent** is a full-stack AI application that lets users upload, preview, and safely modify text-based files using plain English instructions. Powered by Groq's ultra-fast LLM inference (LLaMA3 / Mixtral), the system routes user intent through a structured tool-calling layer before executing any file operation — ensuring controlled, auditable, and secure interactions.

This project demonstrates how to build a **production-grade agentic AI system** with real-world constraints: sandboxed file access, environment-based secrets, backup-before-write policies, and a clean Streamlit UI.

---

## 🚀 Live Demo

🔗 **[Launch App →](https://groq-ai-file-editor.streamlit.app/)**


---

## ✨ Features

- **Natural language file editing** — describe what you want; the agent handles the rest
- **File upload & preview** — view file contents directly in the UI before and after edits
- **Safe, sandboxed operations** — all writes are confined to the `workspace/` directory
- **Automatic backups** — every file is backed up (`.bak`) before modification
- **Downloadable output** — retrieve the edited file instantly after processing
- **Secure key management** — API keys handled via environment variables, never hardcoded

---

## 🏗 Architecture

```
User (Streamlit UI)
        ↓
Groq LLM (Tool Decision Layer)
        ↓
Tool Execution Layer
        ↓
Sandboxed File System (workspace/)
```

**Core Design Principles:**

| Principle | Implementation |
|---|---|
| Sandboxed file access | All I/O restricted to `workspace/` |
| Allowlisted file types | `.txt`, `.md`, `.json`, `.py` only |
| Backup-before-write | `.bak` copy created before every save |
| No direct path control | Users cannot specify raw file paths |
| Secret management | API keys via environment variables |

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| LLM Inference | [Groq API](https://groq.com/) — LLaMA3 / Mixtral |
| UI Framework | [Streamlit](https://streamlit.io/) |
| Language | Python 3.9+ |
| Agent Pattern | Structured tool-calling (function calling) |
| File Operations | Custom sandboxed `file_utils.py` |
| Deployment | Streamlit Cloud |

---

## 🔐 Security

Security is a first-class concern in this project. The following controls are enforced:

- **Directory sandboxing** — file operations are restricted exclusively to `workspace/`
- **Extension allowlist** — only `.txt`, `.md`, `.json`, and `.py` files are accepted
- **File size limits** — uploads above a configurable threshold are rejected
- **Automatic backups** — a `.bak` file is created before any overwrite
- **No user-controlled paths** — users select files from a UI list, never provide raw paths
- **Environment variable secrets** — `GROQ_API_KEY` is never exposed in source code

---

## 📁 Project Structure

```
groq-ai-file-editor/
│
├── app.py               # Streamlit UI — handles uploads, display, and user interaction
├── agent.py             # Groq LLM integration + tool-calling logic
├── file_utils.py        # Secure, sandboxed file read/write operations
├── workspace/           # Runtime directory for editable files
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🛠 Local Setup

### Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/MohanGC07/groq-ai-file-editor.git
cd groq-ai-file-editor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already included in `.gitignore`.

### 5. Run the Application

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## 🌍 Deployment (Streamlit Cloud)

1. Push your repository to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in
3. Click **New App** and connect your repository
4. Set the **main file path** to `app.py`
5. Under **App Settings → Secrets**, add:

```toml
GROQ_API_KEY = "your_api_key_here"
```

6. Click **Deploy** — your app will be live within minutes

---

## 🧪 Example Instructions

Once a file is uploaded, try natural language prompts such as:

```
"Append a motivational quote at the end of the file."
"Rewrite this file in a professional tone."
"Summarize the contents in three bullet points."
"Fix any grammar or spelling errors."
"Format the JSON file with proper indentation."
"Add a header and footer to this markdown file."
```

---

## ⚠️ Limitations

- Only text-based files are supported (`.txt`, `.md`, `.json`, `.py`)
- No persistent storage on Streamlit Cloud — files reset on container restart
- Binary formats (PDF, DOCX, images) are not supported
- Single-file editing only; no batch operations in the current version

---

## 🔮 Roadmap

Planned improvements for future versions:

- [ ] **Diff preview** — show proposed changes before applying them
- [ ] **Undo / version history** — step back through previous file states
- [ ] **Multi-file editing** — apply a single instruction across multiple files
- [ ] **Git integration** — commit changes directly to a repository
- [ ] **Cloud storage** — persist files via S3 or Supabase
- [ ] **User authentication** — role-based access control
- [ ] **Streaming responses** — real-time output as the agent processes

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- **Tool-based agent architecture** — designing LLM systems with structured function calling
- **Secure file system handling** — sandboxing, allowlisting, and backup strategies
- **Groq LLM integration** — leveraging high-speed inference with LLaMA3 / Mixtral
- **Full-stack AI development** — connecting LLM backends to production-ready UIs
- **Secure deployment practices** — environment variables, secret management, cloud hosting

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with a focus on **secure agentic AI systems** and practical deployment patterns.

If you found this project useful, consider giving it a ⭐ on GitHub!

> Questions or suggestions? Open an issue or reach out directly.