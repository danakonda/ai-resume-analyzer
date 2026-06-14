import streamlit as st
import requests
backend="http://localhost:8000"
st.title("AI Resume Analyzer")
uploaded=st.file_uploader("Upload Resume",type=["pdf"])
if uploaded:
    files={
        "file":(uploaded.name,uploaded.getvalue(),"application/pdf")
    }
    requests.post(f"{backend}/upload",files=files)
    st.success("Resume Uploaded")
job=st.text_area("Paste Job Description")
if st.button("Analyze"):
    response=requests.get(f"{backend}/analyze",params={"job_description":job})
    st.write("Status code:",response.status_code)
    data=response.json()
    if response.status_code==200:
        data=response.json()

    else:
        st.error(response.text)
        st.stop()
    st.subheader("Match Score")
    st.metric("ATS Score",data["match_score"])
    st.subheader("Resume Skills")
   
    st.write(data["resume_skills"])
    st.subheader("job_skills")
    st.write(data["job_skills"])
    st.subheader("missing_skills")
    st.write(data["missing_skills"])
    st.subheader("suggestions")
    st.write(data["suggestions"])


   