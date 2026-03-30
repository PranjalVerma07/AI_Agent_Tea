"""Heuristic employee-count estimates by company type.

Derives a stable pseudo-random range from the company name (and optional
company type) so repeated lookups for the same inputs stay consistent.
"""

import hashlib
import random


def estimate_employees(company_name: str, company_type: str | None = None) -> int:
    """
    Estimate employee count.
    Optionally, upgrade to ML model using historical data.
    """
    name_key = company_name.strip()
    seed = int(
        hashlib.sha256(name_key.encode("utf-8")).hexdigest(),
        16,
    ) % (2**32)
    rng = random.Random(seed)
    if company_type == "BPO":
        return rng.randint(100, 500)
    elif company_type == "IT":
        return rng.randint(50, 300)
    else:
        return rng.randint(30, 200)
