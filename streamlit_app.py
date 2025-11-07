import streamlit as st
import requests
import json

st.set_page_config(page_title="Forever Dashboard", page_icon="⏳", layout="wide")

st.title("⏳ Forever Automation Dashboard")

repo_owner = "YOUR_GITHUB_USERNAME"
repo_name = "forever-dashboard"
file_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/data/status.json"

try:
    res = requests.get(file_url)
    res.raise_for_status()
    data = res.json()
    st.success("Latest status loaded successfully!")
except Exception as e:
    st.error(f"Failed to load status: {e}")
    st.stop()

st.write("### 🕒 Last Run Info")
st.json(data)

if st.button("Trigger Manual Run"):
    github_token = st.secrets["GITHUB_TOKEN"]
    workflow = "run_scraper.yml"
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow}/dispatches"
    res = requests.post(url, headers={
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json"
    }, json={"ref": "main"})
    if res.status_code == 204:
        st.success("✅ Workflow triggered successfully!")
    else:
        st.error(f"Failed to trigger: {res.status_code} {res.text}")
