"""Main entry point for the lead-generation workflow."""

import pandas as pd
from agent import chai_ai_agent

if __name__ == "__main__":
    city = input("Enter city for lead generation: ")
    leads = chai_ai_agent(city)

    print("\n--- Generated Leads ---\n")
    for l in leads:
        print(
            f"Company:{l['company']} | Employees: {l['employees']} | "
            f"Machines: {l['machines_required']} | POC: {l['poc_role']} "
            f"({l['contact']})"
        )

    df = pd.DataFrame(leads)
    df.to_csv(f"{city}_tea_leads.csv", index=False)
    print(f"\n✅ Leads exported to {city}_tea_leads.csv")
