# Calculates compatibility score between job description and uploaded resume

def calculate_score(text, keywords):
    text = text.lower()
    matches = sum(1 for k in keywords if k in text)
    return round((matches/len(keywords)) * 100, 2)