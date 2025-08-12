from client_setup import ask_model

def generate_investment_plan(salary, risk_profile, country, news_summary):
    """Generate investment advice based on user profile and latest news"""
    messages = [
        {"role": "system", "content": "You are a professional financial advisor."},
        {"role": "user", "content": f"""
Salary: {salary}
Risk profile: {risk_profile}
Country: {country}
Recent market news summary: {news_summary}

Give me:
1. Recommended asset allocation (% in each category)
2. Top 3 investment instruments in my country
3. Explanation of why this allocation suits my profile
"""}
    ]
    return ask_model(messages)
