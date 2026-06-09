import os
import requests

API_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def get_cv_feedback(cv_text):
	payload = {"inputs": cv_text}
	response = requests.post(API_URL, headers=HEADERS, json=payload)
	return response.json()
