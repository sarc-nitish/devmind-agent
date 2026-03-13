from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(pr_data: dict) -> dict:
    """AI-powered code review using Groq"""
    
    # Prepare files summary
    files_summary = ""
    for file in pr_data["files"]:
        if file["patch"]:
            files_summary += f"\n### File: {file['filename']}\n"
            files_summary += f"Status: {file['status']} | +{file['additions']} -{file['deletions']}\n"
            files_summary += f"```diff\n{file['patch'][:3000]}\n```\n"
    
    prompt = f"""You are an expert code reviewer. Analyze this Pull Request and provide detailed feedback.

PR Title: {pr_data['title']}
PR Description: {pr_data['description']}
Author: {pr_data['author']}
Changes: +{pr_data['total_additions']} -{pr_data['total_deletions']} lines

## Changed Files:
{files_summary}

Provide a structured review with:
1. **Overall Assessment** (Approve/Request Changes/Comment)
2. **Bugs & Issues** (list any bugs found)
3. **Security Vulnerabilities** (any security concerns)
4. **Performance Issues** (optimization opportunities)
5. **Code Quality** (readability, best practices)
6. **Positive Highlights** (what's done well)
7. **Summary** (2-3 line overall summary)

Be specific, actionable, and constructive."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=2000
    )
    
    review_text = response.choices[0].message.content
    
    return {
        "review": review_text,
        "model_used": "llama-3.3-70b-versatile",
        "pr_title": pr_data["title"],
        "author": pr_data["author"],
        "files_reviewed": len(pr_data["files"])
    }


def generate_pr_description(pr_data: dict) -> str:
    """Auto-generate improved PR description"""
    
    files_list = "\n".join([f"- {f['filename']}" for f in pr_data["files"]])
    
    prompt = f"""Based on this PR, generate a professional PR description.

PR Title: {pr_data['title']}
Files Changed:
{files_list}

Generate a clear PR description with:
- What changed
- Why it changed  
- How to test it
Keep it concise and professional."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )
    
    return response.choices[0].message.content