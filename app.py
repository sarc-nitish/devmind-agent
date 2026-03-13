import streamlit as st
from agent.pr_fetcher import fetch_pr_details
from agent.code_reviewer import review_code, generate_pr_description
from agent.report_generator import generate_report

# Page config
st.set_page_config(
    page_title="DevMind - AI Code Review Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title(" DevMind")
st.subheader("AI-Powered Code Review & PR Assistant")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/code-review.png", width=80)
    st.markdown("### About DevMind")
    st.info("""
    DevMind is an AI agent that automatically reviews your GitHub Pull Requests.
    
    **Powered by:**
    -  Llama 3.3 70B (Groq)
    -  GitHub API
    -  Streamlit
    """)
    st.markdown("### How to use")
    st.markdown("""
    1. Paste your GitHub PR URL
    2. Click **Analyze PR**
    3. Get instant AI review!
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    pr_url = st.text_input(
        " GitHub PR URL",
        placeholder="https://github.com/owner/repo/pull/123",
        help="Paste any public GitHub Pull Request URL"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button(" Analyze PR", type="primary", use_container_width=True)

# Analysis
if analyze_btn and pr_url:
    
    # Step 1: Fetch PR
    with st.spinner(" Fetching PR details from GitHub..."):
        try:
            pr_data = fetch_pr_details(pr_url)
            st.success(f"✅ PR fetched: **{pr_data['title']}** by @{pr_data['author']}")
        except Exception as e:
            st.error(f" Error fetching PR: {str(e)}")
            st.stop()
    
    # Step 2: AI Review
    with st.spinner(" AI Agent analyzing your code..."):
        try:
            review_data = review_code(pr_data)
        except Exception as e:
            st.error(f" Error during review: {str(e)}")
            st.stop()
    
    # Step 3: Generate Report
    with st.spinner(" Generating report..."):
        report = generate_report(review_data, pr_data)
    
    st.markdown("---")
    
    # Results
    st.markdown("##  Review Report")
    
    # Metrics row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Status", report["status"])
    m2.metric("Quality Score", f"{report['score']}/100")
    m3.metric("Files Reviewed", len(report["files_reviewed"]))
    m4.metric("Changes", f"+{report['total_additions']} / -{report['total_deletions']}")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([" AI Review", " Files Changed", " Auto PR Description"])
    
    with tab1:
        st.markdown("### AI Review Findings")
        if report["issues_found"]:
            st.warning("**Issues Found:** " + " | ".join(report["issues_found"]))
        st.markdown(report["review_text"])
    
    with tab2:
        st.markdown("### Files Changed")
        for file in report["files_reviewed"]:
            with st.expander(f" {file['filename']} (+{file['additions']} / -{file['deletions']})"):
                if file["patch"]:
                    st.code(file["patch"], language="diff")
                else:
                    st.info("No diff available for this file")
    
    with tab3:
        st.markdown("### Auto-Generated PR Description")
        with st.spinner(" Generating PR description..."):
            pr_desc = generate_pr_description(pr_data)
        st.markdown(pr_desc)
        st.download_button(
            " Copy Description",
            pr_desc,
            file_name="pr_description.md",
            mime="text/markdown"
        )

elif analyze_btn and not pr_url:
    st.warning(" Please enter a GitHub PR URL first!")

# Footer
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ for Microsoft AI Dev Days Hackathon 2026 | Powered by Groq + Llama 3.3</center>",
    unsafe_allow_html=True
)