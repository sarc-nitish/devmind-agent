def generate_report(review_data: dict, pr_data: dict) -> dict:
    """Generate final structured report"""
    
    review_text = review_data["review"]
    
    # Determine severity score
    score = 100
    issues = []
    
    if "bug" in review_text.lower() or "error" in review_text.lower():
        score -= 20
        issues.append("🐛 Bugs detected")
    
    if "security" in review_text.lower() or "vulnerability" in review_text.lower():
        score -= 25
        issues.append("🔒 Security concerns")
    
    if "performance" in review_text.lower():
        score -= 10
        issues.append("⚡ Performance issues")
    
    if "approve" in review_text.lower():
        status = "✅ Approved"
        status_color = "green"
    elif "request changes" in review_text.lower():
        status = "❌ Changes Requested"
        status_color = "red"
    else:
        status = "💬 Needs Discussion"
        status_color = "orange"
    
    return {
        "status": status,
        "status_color": status_color,
        "score": max(score, 0),
        "issues_found": issues,
        "files_reviewed": pr_data["files"],
        "review_text": review_text,
        "pr_title": pr_data["title"],
        "author": pr_data["author"],
        "total_additions": pr_data["total_additions"],
        "total_deletions": pr_data["total_deletions"],
        "model_used": review_data["model_used"]
    }