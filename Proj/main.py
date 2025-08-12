from news_fetcher import fetch_financial_news
from news_summarizer import summarize_news
from investment_advisor import generate_investment_plan
from salary_allocator import salary_allocation

def main():
    # Step 1: Get user profile
    salary = int(input("Enter your monthly salary: "))
    fixed_expenses = int(input("Enter your fixed monthly expenses: "))
    debt = int(input("Enter your total monthly debt payments: "))
    risk_profile = input("Enter your risk profile (conservative/moderate/aggressive): ")
    country = input("Enter your country code (in/jp): ")

    # Step 2: Fetch and summarize news
    print("\nFetching latest financial news...")
    articles = fetch_financial_news(country)
    news_summary = summarize_news(articles)
    print("\n--- Latest Financial News Summary ---")
    print(news_summary)

    # Step 3: Generate investment plan
    investment_plan = generate_investment_plan(salary, risk_profile, country, news_summary)
    print("\n--- Investment Plan ---")
    print(investment_plan)

    # Step 4: Salary allocation
    allocation_plan = salary_allocation(salary, fixed_expenses, debt, country, risk_profile)
    print("\n--- Salary Allocation Plan ---")
    print(allocation_plan)

if __name__ == "__main__":
    main()
