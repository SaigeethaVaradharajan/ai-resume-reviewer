# Import libraries:
import streamlit as st
from parser import extract_text
from job_parser import extract_keywords
from score import calculate_score

# Title:
st.set_page_config(page_title = "AI Resume Reviewer", layout="centered")

# Customizing Layout of Webpage:
st.markdown("""
    <style>
            body{
                background-color: #ffc0cb;
                font-family: 'Segoe UI', Garamond;
            }
            .title{
                font-size: 40px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 20px;      
            }
            .stButton>button{
                background-color: #DA70D6;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
            }
            .stTextArea, .stFileUploader{
                border-radius: 15px;
                background-color: #D8BFD8;
                padding: 10px;
            }
            </style>
            """, unsafe_allow_html=True)
# Use the custom title style
st.markdown('<div class="title">AI Resume Reviewer</div>', unsafe_allow_html=True)

# Add upload resume instructions:
pdf_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])
job_description = st.text_area("Type in the job description")

# Add a button to generate the results:
if st.button("Generate Review"):
    if pdf_file and job_description.strip():
        resume_text = extract_text(pdf_file)
        keywords = extract_keywords(job_description)
        score = calculate_score(resume_text, keywords)

        st.subheader("Results")
        st.write(f"**Compatibility Score:** {score}%")
        st.write("**Extracted Keywords:**")
        st.write(",".join(keywords))


