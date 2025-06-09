import streamlit as st
import pandas as pd


import streamlit as st

st.set_page_config(page_title="RPRB Dashboard Home", layout="wide")
st.title("📊 Ready by Five Data Dashboard")
st.markdown("Welcome! Use this tool to explore program and contract data for FY24 and FY25.")

st.markdown("---")

st.header("🔗 Quick Navigation")

st.markdown("""
- [🏢 **Agency Dashboard**](./Agency_Dashboard)
    - View detailed performance by agency, program, and metric.
- [📄 **Contract Overview**](./Contract_Information)
    - Explore contracts by year, duration, and see target changes.
- [📚 **Metrics Glossary**](./Metrics_Glossary)
    - Understand key metrics, definitions, and categories used.
- [📈 **Metric Trends (FY24–FY25)**](./Metric_Trends)
    - Compare program performance and trends across years.
""")

st.markdown("---")

st.info("💡 Tip: Use filters on each page to narrow results by fiscal year, program, or metric type.")










# st.set_page_config(page_title="Main Dashboard", layout="wide")
# st.title("📊 Agency Performance Summary")

# # --- Load Data ---
# @st.cache_data
# def load_data():
#     return pd.read_excel("agency_program_data.xlsx")

# df = load_data()

# # --- Welcome / Intro ---
# st.markdown("""
# Welcome to the Ready by Five Agency Dashboard 👋  
# Use the sidebar to explore specific service categories, programs, or metrics.
# This main page gives you a high-level view of all agencies and outcomes.

# 🧭 For deeper analysis, explore the **pages on the left**.
# """)



# # --- Optional Overview Stats ---
# st.subheader("🧮 Overall Totals (All Years & Agencies)")
# totals = df.groupby("Metric Type")[["Target", "Actual"]].sum().reset_index()
# totals["Outcome %"] = (totals["Actual"] / totals["Target"]) * 100

# st.dataframe(totals.style.format({"Target": "{:,.0f}", "Actual": "{:,.0f}", "Outcome %": "{:.1f}%"}))








# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(page_title="Agency Dashboard", layout="wide")
# st.title("📊 Agency Performance Overview (FY24 & FY25)")

# # --- Load Excel Data ---
# @st.cache_data
# def load_data():
#     return pd.read_excel("agency_program_data.xlsx")

# df = load_data()

# # --- Sidebar Filters ---
# st.sidebar.header("Filter Data")

# all_years = sorted(df["Fiscal Year"].unique())
# fiscal_years = st.sidebar.multiselect("Fiscal Year", all_years, default=all_years)

# all_agencies = sorted(df["Agency Name"].unique())
# agencies = st.sidebar.multiselect("Agency Name", all_agencies, default=all_agencies)

# all_metrics = sorted(df["Metric Type"].unique())
# metric_types = st.sidebar.multiselect("Metric Type", all_metrics, default=all_metrics)

# filtered_programs = df[df["Agency Name"].isin(agencies)]["Program Name"].unique()
# program_names = st.sidebar.multiselect("Program Name", sorted(filtered_programs), default=sorted(filtered_programs))

# # --- Apply Filters ---
# filtered_df = df[
#     (df["Fiscal Year"].isin(fiscal_years)) &
#     (df["Agency Name"].isin(agencies)) &
#     (df["Metric Type"].isin(metric_types)) &
#     (df["Program Name"].isin(program_names))
# ]

# # --- KPI Section ---
# st.subheader("📌 Summary Metrics")
# col1, col2, col3 = st.columns(3)
# col1.metric("🎯 Total Target", int(filtered_df["Target"].sum()))
# col2.metric("✅ Total Actual", int(filtered_df["Actual"].sum()))
# try:
#     outcome_pct = (filtered_df["Actual"].sum() / filtered_df["Target"].sum()) * 100
#     col3.metric("📈 Overall Outcome %", f"{outcome_pct:.1f}%")
# except ZeroDivisionError:
#     col3.metric("📈 Overall Outcome %", "N/A")

# # --- Bar Chart by Program (only if multiple programs selected) ---
# if len(program_names) > 1:
#     st.subheader("📈 Outcome % by Program")
#     fig = px.bar(
#         filtered_df,
#         x="Program Name",
#         y="Outcome %",
#         color="Contract Duration",
#         hover_data=["Fiscal Year", "Target", "Actual"],
#         title="Program Performance (Grouped by Outcome %)"
#     )
#     fig.update_yaxes(title="Outcome %", tickformat=".0%")
#     st.plotly_chart(fig, use_container_width=True)

# # --- Focused View: Single Program + Agency → Breakdown by Metric Type ---
# if len(program_names) == 1 and len(agencies) == 1:
#     st.subheader(f"📊 {program_names[0]} — Metric Breakdown")

#     metric_breakdown = df[
#         (df["Program Name"] == program_names[0]) &
#         (df["Agency Name"] == agencies[0]) &
#         (df["Fiscal Year"].isin(fiscal_years))
#     ].groupby("Metric Type")[["Target", "Actual"]].sum().reset_index()

#     if not metric_breakdown.empty:
#         fig_metric_breakdown = px.bar(
#             metric_breakdown.melt(id_vars="Metric Type", value_vars=["Target", "Actual"]),
#             x="Metric Type",
#             y="value",
#             color="variable",
#             barmode="group",
#             title=f"{program_names[0]} — Target vs Actual by Metric Type",
#             labels={"value": "Total", "variable": "Type"},
#         )
#         st.plotly_chart(fig_metric_breakdown, use_container_width=True)
#     else:
#         st.info("No data available for the selected Program/Agency.")

# # --- Raw Data Viewer ---
# with st.expander("🗂 View Raw Filtered Data"):
#     st.dataframe(filtered_df)
