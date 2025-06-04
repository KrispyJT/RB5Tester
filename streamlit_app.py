import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Agency Dashboard", layout="wide")
st.title("📊 Agency Performance Overview (FY24 & FY25)")

# --- Load Excel Data ---
@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# --- Filters ---
st.sidebar.header("Filter Data")
fiscal_year = st.sidebar.selectbox("Fiscal Year", sorted(df["Fiscal Year"].unique()))
agency = st.sidebar.selectbox("Agency Name", sorted(df["Agency Name"].unique()))
metric_type = st.sidebar.selectbox("Metric Type", sorted(df["Metric Type"].unique()))

# --- Apply Filters ---
filtered_df = df[
    (df["Fiscal Year"] == fiscal_year) &
    (df["Agency Name"] == agency) &
    (df["Metric Type"] == metric_type)
]


# --- New: Program Name Filter (based on agency selection) ---
program_options = df[df["Agency Name"] == agency]["Program Name"].unique()
program_name = st.sidebar.selectbox("Program Name", sorted(program_options))

# --- New: Filter across both FYs for selected program ---
comparison_df = df[
    (df["Agency Name"] == agency) &
    (df["Program Name"] == program_name) &
    (df["Metric Type"] == metric_type)
]

# --- New: Comparison Chart ---
st.subheader(f"📊 {program_name} - {metric_type} Comparison (FY24 vs FY25)")
fig_compare = px.bar(
    comparison_df,
    x="Fiscal Year",
    y="Outcome %",
    color="Fiscal Year",
    barmode="group",
    text="Outcome %",
    hover_data=["Target", "Actual"],
    title=f"{program_name} - {metric_type} Outcome Comparison by Year"
)
fig_compare.update_traces(texttemplate='%{text:.1%}', textposition='outside')
fig_compare.update_yaxes(title="Outcome %", tickformat=".0%")

st.plotly_chart(fig_compare, use_container_width=True)



# --- KPI Section ---
st.subheader("📌 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("🎯 Target", int(filtered_df["Target"].sum()))
col2.metric("✅ Actual", int(filtered_df["Actual"].sum()))
try:
    outcome_pct = (filtered_df["Actual"].sum() / filtered_df["Target"].sum()) * 100
    col3.metric("📈 Outcome %", f"{outcome_pct:.1f}%")
except ZeroDivisionError:
    col3.metric("📈 Outcome %", "N/A")

# --- Outcome % Chart ---
st.subheader("📈 Outcome % by Program")
fig = px.bar(
    filtered_df,
    x="Program Name",
    y="Outcome %",
    color="Contract Duration",
    hover_data=["Target", "Actual"],
    title=f"{metric_type} Performance - {agency} ({fiscal_year})"
)
st.plotly_chart(fig, use_container_width=True)

# --- Raw Data Viewer ---
with st.expander("🗂 View Raw Filtered Data"):
    st.dataframe(filtered_df)
