from client_setup import ask_model

def summarize_news(articles):
    """Summarize financial news articles"""
    news_text = "\n".join([f"{i+1}. {a['title']} - {a['description']}" for i, a in enumerate(articles)])
    messages = [
        {"role": "system", "content": "You are a financial news summarizer."},
        {"role": "user", "content": f"Summarize the key points and market impact from these news:\n{news_text}"}
    ]
    summary = ask_model(messages)
    return summary
