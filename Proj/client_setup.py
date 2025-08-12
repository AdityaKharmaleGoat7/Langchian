from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def ask_model(messages):
    """Send messages to DeepSeek model via OpenRouter"""
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )
    return completion.choices[0].message.content
