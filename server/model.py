import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to generate AI content
def generate_text(prompt: str) -> str:
    if not OPENAI_API_KEY:
        raise ValueError("Missing OpenAI API Key. Set it in the .env file.")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return response["choices"][0]["message"]["content"]
