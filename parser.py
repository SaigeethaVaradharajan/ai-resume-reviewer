# Import pdfplumber:
import pdfplumber

# Function to extract text from pdf resumes:
def extract_text(file):
    with pdfplumber.open(file) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())