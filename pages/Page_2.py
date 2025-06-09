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

# --- Page Filter ---
st.header("📅 Filter by Fiscal Year")
years = sorted(df["Fiscal Year"].dropna().unique())
selected_year = st.selectbox("Select Fiscal Year", ["All"] + years)

# --- Filter Data ---
filtered_df = df.copy()
if selected_year != "All":
    filtered_df = df[df["Fiscal Year"] == selected_year]

# --- Summary Stats ---
st.subheader("📊 Contract Summary")
summary = filtered_df.groupby("Fiscal Year").agg(
    Agencies=("Agency Name", pd.Series.nunique),
    Programs=("Program Name", pd.Series.nunique),
    Program_Types=("Program Type", pd.Series.nunique)
).reset_index()

st.dataframe(summary)

# --- Pie Charts: Contract Duration by Fiscal Year ---
st.subheader("🥧 Contract Duration Distribution by Year")
unique_contracts = filtered_df.drop_duplicates(subset=["Agency ID", "Program Name", "Fiscal Year", "Contract Duration"])
# Filter and group data
duration_pie_data = unique_contracts.groupby(["Fiscal Year", "Contract Duration"]).size().reset_index(name="Count")

# Create columns for side-by-side pie charts
col1, col2 = st.columns(2)

with col1:
    st.markdown("**FY24 Contract Durations**")
    fy24_data = duration_pie_data[duration_pie_data["Fiscal Year"] == "FY24"]
    fig24 = px.pie(
        fy24_data,
        names="Contract Duration",
        values="Count",
        title="FY24 Distribution",
        hole=0.3
    )
    st.plotly_chart(fig24, use_container_width=True)

with col2:
    st.markdown("**FY25 Contract Durations**")
    fy25_data = duration_pie_data[duration_pie_data["Fiscal Year"] == "FY25"]
    fig25 = px.pie(
        fy25_data,
        names="Contract Duration",
        values="Count",
        title="FY25 Distribution",
        hole=0.3
    )
    st.plotly_chart(fig25, use_container_width=True)


# --- Drilldown: View Programs by Duration ---
st.subheader("🔍 View Programs by Contract Duration")
all_durations = sorted(filtered_df["Contract Duration"].dropna().unique())
selected_duration = st.selectbox("Select Contract Duration to Explore", all_durations)

df_duration = unique_contracts[unique_contracts["Contract Duration"] == selected_duration]

if df_duration.empty:
    st.info("No programs match the selected duration.")
else:
    st.markdown(f"### Programs with **{selected_duration}** contracts")
    st.dataframe(df_duration[[
        "Agency ID", "Agency Name", "Program Name", "Program Type", "Service Category", "Fiscal Year"
    ]].sort_values(by=["Agency Name", "Program Name"]))



##########

# --- Contract Duration Breakdown ---
# st.subheader("⏳ Contract Durations by Year")
# unique_contracts = filtered_df.drop_duplicates(subset=["Agency ID", "Program Name", "Fiscal Year", "Contract Duration"])
# duration_counts = unique_contracts.groupby(["Fiscal Year", "Contract Duration"]).size().reset_index(name="Count")
# pivot = duration_counts.pivot(index="Fiscal Year", columns="Contract Duration", values="Count").fillna(0)

# st.dataframe(pivot)

# # --- Bar Chart ---
# st.subheader("📈 Contract Duration Distribution")
# fig = px.histogram(
#     unique_contracts,
#     x="Contract Duration",
#     color="Fiscal Year",
#     barmode="group",
#     title="Distribution of Unique Contract Durations by Year"
# )
# st.plotly_chart(fig, use_container_width=True)

#####



# --- Section: Load Preprocessed Target Changes CSV ---
st.subheader("📈 Target Changes from FY24 to FY25")

@st.cache_data
def load_target_change():
    return pd.read_excel("Target_Change_by_Metric.xlxs")

try:
    target_df = load_target_change()

    # Optional filter
    metric_options = sorted(target_df["Metric Type"].dropna().unique())
    selected_metric = st.selectbox("Filter by Metric Type", ["All"] + metric_options)

    plot_df = target_df.copy()
    if selected_metric != "All":
        plot_df = plot_df[plot_df["Metric Type"] == selected_metric]

    if plot_df.empty:
        st.warning("No data available for selected metric.")
    else:
        # Bar chart of Target Change
        fig = px.bar(
            plot_df,
            x="Agency Name",
            y="Target Change",
            color="Metric Type",
            title="Change in Metric Targets (FY25 - FY24)",
            labels={"Target Change": "Target Difference"},
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📄 Show Source Data"):
            st.dataframe(plot_df)

except FileNotFoundError:
    st.warning("⚠️ Could not find 'Targets Change by Metric.csv'. Please make sure the file is in the app directory.")















