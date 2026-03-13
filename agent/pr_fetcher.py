from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_pr_details(pr_url: str) -> dict:
    """Fetch PR details from GitHub"""
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    
    # Parse PR URL
    # Format: https://github.com/owner/repo/pull/123
    parts = pr_url.strip("/").split("/")
    owner = parts[-4]
    repo_name = parts[-3]
    pr_number = int(parts[-1])
    
    repo = g.get_repo(f"{owner}/{repo_name}")
    pr = repo.get_pull(pr_number)
    
    # Get all changed files
    files_data = []
    for file in pr.get_files():
        files_data.append({
            "filename": file.filename,
            "status": file.status,
            "additions": file.additions,
            "deletions": file.deletions,
            "patch": file.patch if file.patch else ""
        })
    
    return {
        "title": pr.title,
        "description": pr.body or "",
        "author": pr.user.login,
        "base_branch": pr.base.ref,
        "head_branch": pr.head.ref,
        "files": files_data,
        "total_additions": pr.additions,
        "total_deletions": pr.deletions
    }