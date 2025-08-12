import streamlit as st
from news_fetcher import fetch_financial_news
from news_summarizer import summarize_news
from investment_advisor import generate_investment_plan
from salary_allocator import salary_allocation

st.set_page_config(page_title="AI Investment Advisor", page_icon="💰", layout="wide")

st.title("💰 AI-Powered Personal Investment Advisor")

# Sidebar for user input
st.sidebar.header("User Profile")
salary = st.sidebar.number_input("Monthly Salary", min_value=1000, step=1000)
fixed_expenses = st.sidebar.number_input("Fixed Monthly Expenses", min_value=0, step=500)
debt = st.sidebar.number_input("Monthly Debt Payments", min_value=0, step=500)
risk_profile = st.sidebar.selectbox("Risk Profile", ["conservative", "moderate", "aggressive"])
country = st.sidebar.selectbox("Country", ["in", "jp"])

if st.sidebar.button("Generate Plan"):
    with st.spinner("Fetching latest news and generating plan..."):
        # Fetch & summarize news
        articles = fetch_financial_news(country)
        news_summary = summarize_news(articles)

        # Generate plans
        investment_plan = generate_investment_plan(salary, risk_profile, country, news_summary)
        allocation_plan = salary_allocation(salary, fixed_expenses, debt, country, risk_profile)

    # Display results
    st.subheader("📢 Latest Financial News Summary")
    st.write(news_summary)

    st.subheader("📈 Investment Plan")
    st.write(investment_plan)

    st.subheader("📊 Salary Allocation Plan")
    st.write(allocation_plan)

else:
    st.info("Fill in your profile in the sidebar and click 'Generate Plan'.")

