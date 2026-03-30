"""Build tea-vending sales leads for a city.

Orchestrates company discovery, employee estimates, machine recommendations,
and POC lookup into one result per company.
"""

from scraper import get_companies
from estimator import estimate_employees
from recommender import infer_company_type, recommend_machines
from poc_finder import find_poc


def chai_ai_agent(city):
    """Return one lead dict per company for the given city."""
    mock_companies = get_companies(city)
    results = []
    for company in mock_companies:
        # `scraper.get_companies()` returns {"company": ..., "address": ...}
        name = company["company"]
        company_type = infer_company_type(name)
        employees = estimate_employees(name, company_type)
        recommendation = recommend_machines(employees, company_type)
        poc = find_poc(name)
        results.append({
            "company": name,
            "address": company["address"],
            "employees": employees,
            "company_type": company_type,
            "tea_consumption_per_day": recommendation["tea_consumption"],
            "machines_required": recommendation["machines_needed"],
            "poc_role": poc["role"],
            "contact": poc["email"]
        })
    return results
