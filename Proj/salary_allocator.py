# salary_allocator.py
from client_setup import ask_model

def salary_allocation(salary, fixed_expenses, debt, country, risk_profile):
    """Plan how to split monthly salary into expenses, debt, emergency, investments"""
    messages = [
        {"role": "system", "content": "You are a salary allocation planner who maximizes long-term returns while respecting risk appetite and country-specific constraints."},
        {"role": "user", "content": f"""
Salary: {salary}
Fixed monthly expenses: {fixed_expenses}
Debt: {debt}
Country: {country}
Risk profile: {risk_profile}

Plan a practical monthly allocation:
- Emergency fund
- Debt repayment
- Taxes
- Fixed expenses
- Investments (break down into asset classes)
- Explain reasoning in simple words
"""}
    ]
    return ask_model(messages)
