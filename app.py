# Import libraries:
import streamlit as st
from parser import extract_text
from job_parser import extract_keywords
from score import score

# Title:
st.set_page_config(page_title = "AI Resume Reviewer", layout="centered")
st.title("AI Resume Reviewer")

# Add upload resume instructions:
pdf_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])
job_description = st.text_area("Type in the job description")

if st.button("Generate Review"):
    if pdf_file and job_description.strip():
        resume_text = extract_text(pdf_file)
        keywords = extract_keywords(job_description)
        score = score(pdf_file, keywords)

        st.subheader("Results")
        st.write(f"**Compatibility Score:** {score}%")
        st.write("**Extracted Keywords:".join(keywords))

    else:
        st.warning("Error! Upload a redsume and enter a job description")


