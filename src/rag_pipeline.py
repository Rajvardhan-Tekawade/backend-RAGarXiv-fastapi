# backend/src/rag_pipeline.py

import requests

# Your Hugging Face API Key (replace with your actual access token/API Key)
HUGGING_FACE_API_KEY = "<Your-Hugging-Face-API-Key>"
MODEL_NAME = "facebook/bart-large-cnn"  # Set the model to BART

# The API URL to call for inference
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

# Function to generate summaries using Hugging Face's hosted API
def generate_summary(text: str):
    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"  # Bearer token for authentication
    }

    payload = {
        "inputs": text
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]  # Return the summary text
    else:
        return f"Error: {response.status_code} - {response.text}"
