import pickle
import re
import joblib
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("model/url_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Preprocess URL (Same as in training)
def preprocess_url(url):
    url = re.sub(r"https?://", "", url)  # Remove http or https
    url = re.sub(r"www\.", "", url)  # Remove www.
    return url

@app.route("/check_url", methods=["POST"])
def check_url():
    try:
        data = request.json
        url = preprocess_url(data["url"])  # Preprocess URL
        vectorized_url = vectorizer.transform([url])  # Convert to TF-IDF features
        prediction = model.predict(vectorized_url)[0]  # Predict using ML model
        
        return jsonify({"is_malicious": bool(prediction)})  # Return result (True if malicious, False if safe)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
