

# st.set_page_config(page_title="Contract Overview", layout="wide")
# st.title("📄 Contract Overview by Fiscal Year")

# # --- Load Data ---
# @st.cache_data
# def load_data():
#     return pd.read_excel("agency_program_data.xlsx")

# df = load_data()

# # --- Sidebar Filter ---
# st.sidebar.header("Filter")
# years = sorted(df["Fiscal Year"].dropna().unique())
# selected_year = st.sidebar.selectbox("Fiscal Year", ["All"] + years)

# # --- Filter Data ---
# if selected_year != "All":
#     df = df[df["Fiscal Year"] == selected_year]

# # --- Summary Stats ---
# st.subheader("📊 Contract Summary")
# summary = df.groupby("Fiscal Year").agg(
#     Agencies=("Agency ID", pd.Series.nunique),
#     Programs=("Program Name", pd.Series.nunique),
#     Service_Categories=("Service Category", pd.Series.nunique)
# ).reset_index()

# st.dataframe(summary)

# # --- Contract Duration Breakdown ---
# st.subheader("⏳ Contract Durations by Year")
# duration_counts = df.groupby(["Fiscal Year", "Contract Duration"]).size().reset_index(name="Count")
# pivot = duration_counts.pivot(index="Fiscal Year", columns="Contract Duration", values="Count").fillna(0)
# st.dataframe(pivot)

# # --- Optional: Visual Chart ---
# st.subheader("📈 Contract Duration Distribution")
# import plotly.express as px
# fig = px.histogram(
#     df,
#     x="Contract Duration",
#     color="Fiscal Year",
#     barmode="group",
#     title="Distribution of Contract Durations by Year"
# )
# st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Contract Overview", layout="wide")
st.title("📄 Contract Overview by Fiscal Year")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# --- Sidebar Filter ---
st.sidebar.header("Filter")
years = sorted(df["Fiscal Year"].dropna().unique())
selected_year = st.sidebar.selectbox("Fiscal Year", ["All"] + years)

# --- Filter Data ---
if selected_year != "All":
    df = df[df["Fiscal Year"] == selected_year]

# --- Summary Stats ---
st.subheader("📊 Contract Summary")
summary = df.groupby("Fiscal Year").agg(
    Agencies=("Agency ID", pd.Series.nunique),
    Programs=("Program Name", pd.Series.nunique),
    Service_Categories=("Service Category", pd.Series.nunique)
).reset_index()
st.dataframe(summary)

# --- Contract Duration Breakdown (Unique Contracts Only) ---
st.subheader("⏳ Contract Durations by Year")

# Drop duplicates to count each contract once per year
unique_contracts = df.drop_duplicates(subset=["Agency ID", "Program Name", "Fiscal Year", "Contract Duration"])

duration_counts = unique_contracts.groupby(["Fiscal Year", "Contract Duration"]).size().reset_index(name="Count")
pivot = duration_counts.pivot(index="Fiscal Year", columns="Contract Duration", values="Count").fillna(0)
st.dataframe(pivot)


# --- Bar Chart ---
st.subheader("📈 Contract Duration Distribution")
fig = px.histogram(
    unique_contracts,
    x="Contract Duration",
    color="Fiscal Year",
    barmode="group",
    title="Distribution of Unique Contract Durations by Year"
)

st.plotly_chart(fig, use_container_width=True)

# --- Drilldown: View Programs by Duration ---
st.subheader("🔍 View Programs by Contract Duration")
all_durations = sorted(df["Contract Duration"].dropna().unique())
selected_duration = st.selectbox("Select Contract Duration to Explore", all_durations)

df_duration = unique_contracts[unique_contracts["Contract Duration"] == selected_duration]

if df_duration.empty:
    st.info("No programs match the selected duration.")
else:
    st.markdown(f"### Programs with **{selected_duration}** contracts")
    st.dataframe(df_duration[[
        "Agency ID", "Agency Name", "Program Name", "Program Type", "Service Category", "Fiscal Year"
    ]].sort_values(by=["Agency Name", "Program Name"]))
