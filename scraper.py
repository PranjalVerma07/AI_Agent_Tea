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
    {"company": "Infosys Limited", "address": "Electronic City, Bangalore", "rating": 4.6},
    {"company": "Tata Consultancy Services (TCS)", "address": "Noida, Uttar Pradesh", "rating": 4.5},
    {"company": "Wipro Limited", "address": "Electronic City, Bangalore", "rating": 4.4},
    {"company": "HCL Technologies", "address": "Noida, Uttar Pradesh", "rating": 4.5},
    {"company": "Tech Mahindra", "address": "Noida, Uttar Pradesh", "rating": 4.3},
    {"company": "LTIMindtree", "address": "Bengaluru, Karnataka", "rating": 4.4},
    {"company": "Accenture India", "address": "Gurugram, Haryana", "rating": 4.6},
    {"company": "Capgemini India", "address": "Noida, Uttar Pradesh", "rating": 4.4},
    {"company": "Cognizant Technology Solutions", "address": "Chennai, Tamil Nadu", "rating": 4.3},
    {"company": "IBM India", "address": "Bangalore, Karnataka", "rating": 4.6},
    {"company": "Oracle India", "address": "Bangalore, Karnataka", "rating": 4.5},
    {"company": "Microsoft India", "address": "Hyderabad, Telangana", "rating": 4.8},
    {"company": "Google India", "address": "Bangalore, Karnataka", "rating": 4.9},
    {"company": "Amazon Development Centre", "address": "Hyderabad, Telangana", "rating": 4.7},
    {"company": "Adobe India", "address": "Noida, Uttar Pradesh", "rating": 4.7},
    {"company": "Dell Technologies", "address": "Bangalore, Karnataka", "rating": 4.4},
    {"company": "HP Enterprise", "address": "Bangalore, Karnataka", "rating": 4.3},
    {"company": "Cisco Systems India", "address": "Bangalore, Karnataka", "rating": 4.6},
    {"company": "Intel India", "address": "Bangalore, Karnataka", "rating": 4.7},
    {"company": "Nokia Solutions", "address": "Noida, Uttar Pradesh", "rating": 4.2},
    {"company": "Ericsson India", "address": "Noida, Uttar Pradesh", "rating": 4.3},
    {"company": "Genpact", "address": "Gurugram, Haryana", "rating": 4.2},
    {"company": "Concentrix", "address": "Gurugram, Haryana", "rating": 4.1},
    {"company": "Teleperformance India", "address": "Noida, Uttar Pradesh", "rating": 4.0},
    {"company": "Conduent India", "address": "Noida, Uttar Pradesh", "rating": 4.0},
    {"company": "Coforge Limited", "address": "Noida, Uttar Pradesh", "rating": 4.3},
    {"company": "Persistent Systems", "address": "Pune, Maharashtra", "rating": 4.4},
    {"company": "Mphasis", "address": "Bangalore, Karnataka", "rating": 4.2},
    {"company": "Hexaware Technologies", "address": "Noida, Uttar Pradesh", "rating": 4.2},
    {"company": "Birlasoft", "address": "Noida, Uttar Pradesh", "rating": 4.1},
]

    kw = keyword.strip().lower()
    filtered_companies = [
        c
        for c in mock_companies
        if city.lower() in c["address"].lower()
        and (not kw or kw in c["company"].lower())
    ]

    return filtered_companies
