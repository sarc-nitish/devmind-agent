# DevMind - Architecture Diagram

## System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACE                        │
│                  Streamlit Web App                       │
└─────────────────────┬───────────────────────────────────┘
                      │ PR URL Input
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  AGENT ORCHESTRATOR                      │
│                     app.py                              │
└──────┬──────────────┬──────────────────┬────────────────┘
       │              │                  │
       ▼              ▼                  ▼
┌──────────┐  ┌──────────────┐  ┌──────────────────┐
│PR Fetcher│  │Code Reviewer │  │Report Generator  │
│          │  │              │  │                  │
│GitHub API│  │ Groq API     │  │Score + Analysis  │
│          │  │Llama 3.3 70B │  │                  │
└──────────┘  └──────────────┘  └──────────────────┘
       │              │                  │
       └──────────────┴──────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  FINAL REPORT                           │
│         Bug Report + Security + Quality Score           │
└─────────────────────────────────────────────────────────┘
```

## Data Flow
1. User pastes GitHub PR URL
2. PR Fetcher fetches all changed files via GitHub API
3. Code Reviewer sends code to Llama 3.3 70B via Groq
4. AI analyzes bugs, security, performance
5. Report Generator calculates quality score
6. Results displayed in Streamlit UI

## Technologies
| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Model | Llama 3.3 70B |
| AI API | Groq |
| Code Fetch | GitHub API |
| Language | Python 3.12 |
| Deployment | Azure App Service |