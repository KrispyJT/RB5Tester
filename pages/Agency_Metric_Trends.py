import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📈 Metric Target Changes", layout="wide")
st.title("📈 Changes in Metric Targets Between Fiscal Years")

@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# Filter to only FY24 and FY25
df = df[df["Fiscal Year"].isin(["FY24", "FY25"])]

# Sidebar filters
st.sidebar.header("Filter")
selected_metric = st.sidebar.selectbox("Metric Type", ["All"] + sorted(df["Metric Type"].dropna().unique()))
selected_agency = st.sidebar.selectbox("Agency Name", ["All"] + sorted(df["Agency Name"].dropna().unique()))

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
    values=["Target", "Contract Duration"],
    aggfunc="first"
).reset_index()

# Flatten columns
pivot_df.columns = [' '.join(col).strip() if col[1] else col[0] for col in pivot_df.columns.values]
# Ensure contract duration columns are numeric
# Convert "9 Months", "12 Months", etc. to integers
pivot_df["Contract Duration FY24"] = pivot_df["Contract Duration FY24"].str.extract(r"(\d+)").astype(float)
pivot_df["Contract Duration FY25"] = pivot_df["Contract Duration FY25"].str.extract(r"(\d+)").astype(float)

# Now safely compute the change
pivot_df["Duration Change"] = pivot_df["Contract Duration FY25"] - pivot_df["Contract Duration FY24"]


# Calculate changes
pivot_df["Target Change"] = pivot_df["Target FY25"] - pivot_df["Target FY24"]
pivot_df["Duration Change"] = pivot_df["Contract Duration FY25"] - pivot_df["Contract Duration FY24"]

# Display data
st.subheader("📊 Agencies Funded in Both FY24 and FY25")
st.dataframe(pivot_df)

# Plot target changes
st.subheader("🔺 Change in Targets")
fig1 = px.bar(
    pivot_df,
    x="Agency Name",
    y="Target Change",
    color="Metric Type",
    title="Change in Metric Targets (FY25 - FY24)",
    labels={"Target Change": "Target Difference"}
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

# Plot duration changes
st.subheader("🕒 Change in Contract Duration")
fig2 = px.bar(
    pivot_df,
    x="Agency Name",
    y="Duration Change",
    color="Metric Type",
    title="Change in Contract Duration (Months)",
    labels={"Duration Change": "Duration Difference (Months)"}
)
fig2.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig2, use_container_width=True)

# Optional: Show raw table
with st.expander("📄 Show Raw Comparison Table"):
    st.dataframe(pivot_df)
