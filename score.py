# Calculates compatibility score between job description and uploaded resume

def score(resume, keywords):
    resume = resume.lower()
    matches = sum(1 for k in keywords if k in resume)
    return round((matches/len(keywords)) * 100, 2)