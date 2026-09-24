import openai
import os
from dotenv import dotenv_values

# .env file se API key load karna
env_vars = dotenv_values(".env")
openai.api_key = env_vars.get("OPENAI_API_KEY")

def ask_gpt(prompt):
    """GPT-4 se jawab laane ka function"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
