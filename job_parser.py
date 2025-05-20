# Import libraries:
from sklearn.feature_extraction.text import TfidfVectorizer 

# Function to extract key words:
def extract_keywords(job_description, max_features=35):
    vector = TfidfVectorizer(stop_words='english', max_features=max_features)
    vector.fit_transform([job_description])
    return vector.get_feature_names_out()


