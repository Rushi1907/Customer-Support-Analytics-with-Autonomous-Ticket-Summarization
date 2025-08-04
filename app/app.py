import streamlit as st
import pandas as pd
from agent.summarizer import summarize_ticket  # make sure path is correct

st.set_page_config(page_title="Customer Support Analyzer", layout="wide")
st.title("📩 Customer Support Analytics + Summarizer")

uploaded_file = st.file_uploader("Upload customer support tickets (CSV)", type="csv")
