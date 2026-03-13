#  DevMind - AI-Powered Code Review Agent

> Built for Microsoft AI Dev Days Hackathon 2026

DevMind is an intelligent AI agent that automatically reviews GitHub Pull Requests, detects bugs, security vulnerabilities, and performance issues using LLama 3.3 70B.

##  Problem Statement
Code reviews are time-consuming and inconsistent. Developers spend hours reviewing PRs manually, often missing critical bugs and security issues.

##  Solution
DevMind automates the entire code review process using AI — just paste a GitHub PR URL and get instant, detailed feedback in seconds.

##  Features
-  **Automated Code Review** — AI analyzes every changed file
-  **Bug Detection** — Identifies potential bugs and errors
-  **Security Analysis** — Flags security vulnerabilities
-  **Performance Review** — Suggests performance improvements
-  **Auto PR Description** — Generates professional PR descriptions
-  **Quality Score** — Gives a 0-100 quality score

##  Architecture
```
GitHub PR URL → PR Fetcher → AI Review Agent → Report Generator → Streamlit UI
                    ↓              ↓
               GitHub API      Groq API
                            (Llama 3.3 70B)
```

##  Tech Stack
- **AI Model:** Llama 3.3 70B via Groq
- **Framework:** Python + Streamlit
- **APIs:** GitHub API, Groq API
- **Deployment:** Azure App Service

##  Quick Start

### Prerequisites
- Python 3.12+
- Groq API Key
- GitHub Personal Access Token

### Installation
```bash
git clone https://github.com/sarc-nitish/devmind-agent.git
cd devmind-agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration
```bash
cp .env.example .env
# Add your API keys in .env file
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

### Run
```bash
streamlit run app.py
```

##  Demo
The agent analyzes real GitHub PRs and provides:
- Overall assessment (Approve/Request Changes)
- Detailed bug and security findings
- Quality score out of 100
- Auto-generated PR description



##  Author
**Nitish Kumar** — Microsoft AI Dev Days Hackathon 2026