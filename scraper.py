"""Company data lookup stub used as a scraper replacement with mock results."""


def get_companies(city, keyword=""):
    """
    Returns a list of dummy companies for a given city.
    Parameters:
        city (str): City name input by user
        keyword (str): Optional substring filter on company name (empty = no filter)
    Returns:
        List[dict]: List of companies with name, address, and rating
    """
    # You can expand this list with more mock companies if needed
    mock_companies = [
        {"company": "ABC Tech Pvt Ltd", "address": "Sector 18, Noida", "rating": 4.5},
        {"company": "XYZ BPO Solutions", "address": "Sector 62, Gurgaon", "rating": 4.2},
        {"company": "NextGen Industries", "address": "Sector 135, Noida", "rating": 4.0},
        {"company": "Future Innovations Ltd", "address": "Sector 21, Delhi", "rating": 4.3},
        {"company": "Global Tech Solutions", "address": "Sector 50, Bangalore", "rating": 4.1},
    ]

    kw = keyword.strip().lower()
    filtered_companies = [
        c
        for c in mock_companies
        if city.lower() in c["address"].lower()
        and (not kw or kw in c["company"].lower())
    ]

    return filtered_companies
