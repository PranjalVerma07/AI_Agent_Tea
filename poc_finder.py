"""Derive a simple point-of-contact estimate from a company name."""


def find_poc(company_name):
    """Return a placeholder HR POC role and email derived from ``company_name``."""
    domain = company_name.lower().replace(" ", "").replace("pvtltd", "") + ".com"
    return {"role": "HR/Admin Manager", "email": f"hr@{domain}"}
