import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📈 Metric Target Changes", layout="wide")
st.title("📈 Metric Target Changes Between Fiscal Years")

@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# Filter to only FY24 and FY25
df = df[df["Fiscal Year"].isin(["FY24", "FY25"])]

# --- Inline Filters ---
st.markdown("### 🔍 Filter Data")
col1, col2 = st.columns(2)

with col1:
    selected_metric = st.selectbox("Select Metric Type", ["All"] + sorted(df["Metric Type"].dropna().unique()))
with col2:
    selected_agency = st.selectbox("Select Agency Name", ["All"] + sorted(df["Agency Name"].dropna().unique()))

# Optional filters
if selected_metric != "All":
    df = df[df["Metric Type"] == selected_metric]
if selected_agency != "All":
    df = df[df["Agency Name"] == selected_agency]

# Identify agencies with records in both FY24 and FY25
agency_fy_counts = df.groupby(["Agency ID", "Metric Type"])["Fiscal Year"].nunique().reset_index()
both_years = agency_fy_counts[agency_fy_counts["Fiscal Year"] == 2]
df_filtered = df.merge(both_years[["Agency ID", "Metric Type"]], on=["Agency ID", "Metric Type"])

# Pivot for target comparison
pivot_df = df_filtered.pivot_table(
    index=["Agency ID", "Agency Name", "Program Name", "Metric Type"],
    columns="Fiscal Year",
    values="Target",
    aggfunc="first"
).reset_index()

# Flatten columns
pivot_df.columns = [' '.join(col).strip() if col[1] else col[0] for col in pivot_df.columns.values]

# Calculate target change
pivot_df["Target Change"] = pivot_df["Target FY25"] - pivot_df["Target FY24"]

# --- Chart: Target Change by Metric ---
st.subheader("📊 Change in Metric Targets")
fig = px.bar(
    pivot_df,
    x="Agency Name",
    y="Target Change",
    color="Metric Type",
    title="Change in Metric Targets (FY25 - FY24)",
    labels={"Target Change": "Target Difference"}
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# --- Optional Raw Table ---
with st.expander("📄 View Raw Data"):
    st.dataframe(pivot_df.sort_values(by=["Metric Type", "Agency Name"]))