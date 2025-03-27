import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset (You can get a dataset from Kaggle)
data = pd.read_csv("ml-api\malicious_urls.csv")  # Ensure the dataset has 'url' and 'label' columns

# Preprocess URLs (Remove http, https, www)
def preprocess_url(url):
    url = re.sub(r"https?://", "", url)  # Remove http or https
    url = re.sub(r"www\.", "", url)  # Remove www.
    return url

data["url"] = data["url"].apply(preprocess_url)

# Feature Extraction using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["url"])
y = data["type"]  # 1 = malicious, 0 = safe

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model and vectorizer
joblib.dump(model, "model/url_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained and saved successfully!")
