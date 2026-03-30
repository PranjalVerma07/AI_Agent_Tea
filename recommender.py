"""Recommend tea-vending machine requirements based on company type and employee count."""


def infer_company_type(company_name):
    """Guess company type from name."""
    name = company_name.lower()
    if "bpo" in name or "solutions" in name:
        return "BPO"
    elif "tech" in name or "software" in name:
        return "IT"
    else:
        return "General"

def estimate_tea_consumption(employees, company_type, shifts="general"):
    """Estimate daily tea cups from headcount, company type, and shift pattern."""
    if company_type == "IT":
        cups_per_emp = 2
    elif company_type == "BPO":
        cups_per_emp = 4
    else:
        cups_per_emp = 3

    if shifts == "24x7":
        cups_per_emp += 1

    total_cups = employees * cups_per_emp
    return total_cups

def recommend_machines(employees, company_type, shifts="general"):
    """Return estimated daily cups and number of machines needed for the given workforce."""
    total_cups = estimate_tea_consumption(employees, company_type, shifts)
    machine_capacity = 100  # cups/day per machine
    machines = total_cups // machine_capacity
    if machines == 0:
        machines = 1
    return {"tea_consumption": total_cups, "machines_needed": machines}
