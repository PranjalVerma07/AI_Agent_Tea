"""Streamlit dashboard for the AI tea vending leads generator.

Enter a city to run the agent, view lead rows in a table, and download CSV.
"""

import streamlit as st
import pandas as pd
from agent import chai_ai_agent

st.title("AI Tea Vending Leads Generator")
city = st.text_input("Enter city:")
if city:
    leads = chai_ai_agent(city)
    df = pd.DataFrame(leads)
    st.dataframe(df)
    st.download_button("Download CSV", df.to_csv(index=False), f"{city}_leads.csv")
