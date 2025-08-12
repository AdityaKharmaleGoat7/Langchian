import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_financial_news(country="in"):
    """Fetch latest financial news for the given country"""
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = [
        {"title": art["title"], "description": art["description"]}
        for art in data.get("articles", [])
    ]
    return articles
