import requests
import json
import os

class LLMBrain:
    def __init__(self, use_real_api=False):
        self.api_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
        self.use_real_api = use_real_api
        self.model = "llama3"  # or 'mistral-uncensored'

    def generate_response(self, user_text, personality_prompt):
        """
        Generates a text response based on user input and the defined personality.
        """
        full_prompt = f"System: {personality_prompt}\nUser: {user_text}\nAssistant:"
        
        if not self.use_real_api:
            # Mock response for testing
            return f"[Simulated LLM Response] I heard you say '{user_text}'. I am responding as your companion."

        try:
            payload = {
                "model": self.model,
                "prompt": full_prompt,
                "stream": False
            }
            response = requests.post(self.api_url, json=payload)
            if response.status_code == 200:
                return response.json().get('response', '')
            else:
                return "Error: LLM backend is offline."
        except Exception as e:
            return f"Connection error: {e}"
