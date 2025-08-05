from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})
    print(f"Assistant: {response}")

# print(messages)

