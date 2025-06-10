import streamlit as st
import pandas as pd

st.set_page_config(page_title="RPRB Dashboard Home", layout="wide")
st.title("📊 Ready by Five Data Dashboard")

st.markdown("""
Welcome! This dashboard explores key metrics, programs, and performance across Fiscal Years 2024 and 2025.

Use the navigation menu on the left to jump into each section.
""")

st.markdown("---")
# --------------------------
st.header("🔗 Quick Navigation")
st.markdown("""
- [📊 **Agency Performance Dashboard**](./Agency_Performance_Dashboard)
    - View detailed performance by agency, program, and metric.
- [🧾 **Agency Program Summary**](./Agency_Program_Summary)  
    - Compare program performance and trends across years.
- [📄 **Contract Overview**](./Contract_Overview)
    - Explore contracts by year, duration, and see target changes.
- [📈 **Metric Trends (FY24–FY25)**](./Metric_Trends_(FY24_vs_FY25))
    - Compare program performance and trends across years.
- [🧭 **Program Explorer by Category**](./Program_Explorer_by_Category) 
    - Compare program performance and trends across years. 
""")
# st.page_link('./Metrics_Glossary.py', disabled=True)

st.info("💡 Tip: Use filters on each page to narrow results by fiscal year, program, or metric type.")
st.markdown("---")
st.info("Click each section below to expand and learn more about key metrics and service categories.")
# --------------------------
st.header("📅 Contract Periods")

with st.expander("📆 Fiscal Year Definitions"):
    st.markdown("""
    - **FY24**  
      • *10/1/2023 – 9/30/2024*  
      • Most programs began 1/1/2024  

    - **FY25**  
      • *10/1/2024 – 9/30/2025*  
      • Current contracts in progress, Indivdiuals Served and Encounters are most recent numbers.  

    - **FY26** *(Upcoming)*  
      • *10/1/2025 – 9/30/2026*  
      • Proposed programs and funding currently under review  
    """)

# --------------------------
st.header("📏 Key Metric Types")

with st.expander("🔹 Individuals Served (IS)"):
    st.markdown("""
    Represents the **number of distinct individuals** served by a program. 
    - Counted once per program per fiscal year  
    - May be duplicated in **Play & Learn** sessions
    Used across ON, HD, PES, and some EL programs.
    - In **Play and Learn**, this may be duplicated (attendees can be counted more than once).

    > Helps measure broad reach — each individual only counted once per program and fiscal year.
    """)

with st.expander("🔹 Encounters"):
    st.markdown("""
    Measures **how often** services were delivered.
    - Tracks how often services were delivered  
    - Includes 1:1 visits, group sessions, classes  
    - Used for frequency/intensity insight
    """)

with st.expander("🔹 Target / Actual / Outcome"):
    st.markdown("""
    - **Target** = What was planned  
    - **Actual** = What occurred  
    - **Outcome %** = Calculated as `Actual / Target × 100` 
    
    Targets are **contractual goals**. Outcomes indicate progress toward these goals.
    """)

with st.expander("🎯 Target Setting"):
    st.markdown("""
    - Targets are set during contract negotiations  
    - Dashboards reflect progress vs these goals  
    """)

with st.expander("📎 Duplicated vs Unduplicated"):
    st.markdown("""
    - **Unduplicated** = Unique persons  
    - **Duplicated** = People counted each time (e.g. Play & Learn)  
    """)

# --------------------------
st.header("🧩 Service Category Guide")

st.markdown("""
These categories help group programs by their intent and delivery approach.
""")

with st.expander("Outreach and Navigation (ON)"):
    st.markdown("""
    Connects families to resources.  
    Providers connect expectant parents and families of young children to early childhood information, programming, and community resources to help foster a healthy, safe, and nurturing environment.

    ➤ Focus: **Referrals** & **Individuals Served**
    """)

with st.expander("Early Learning (EL)"):
    st.markdown("""
    Supports cognitive and social development.
    Programming supports children’s cognitive, social, and emotional development while increasing parents’ and other adult caregivers’ knowledge and skills in supporting children’s early learning development.
  
    ➤ Focus: **Encounters**, Play & Learn sessions
    """)

with st.expander("Healthy Development (HD)"):
    st.markdown("""
    Supports physical and emotional well-being.  
    Providers ensure expectant parents and those with young children have access to comprehensive and coordinated care that optimizes physical and emotional health. Programming follows evidence-based practices that demonstrate success in supporting positive health behaviors for expectant mothers and children.
    ➤ Focus: **Encounters** & **Individuals Served**
    """)

with st.expander("Parent Education and Support (PES)"):
    st.markdown("""
    Home and community-based parenting education.
    Services ensure parents have the knowledge and skills to support their children’s health, development, and learning. PE programs provide in-home and/or community-based support and education. In-home services involve trained providers visiting families’ homes to offer one-on-one education and support. 
    ➤ Focus: **Encounters** & **Individuals Served**
    """)

# --------------------------
st.markdown("---")
st.markdown("📎 [Visit First Steps Kent Provider Page](https://www.firststepskent.org/millage/providers) for more details.")








#####


# st.set_page_config(page_title="RPRB Dashboard Home", layout="wide")
# st.title("📊 Ready by Five Data Dashboard")
# st.markdown("Welcome! Use this tool to explore program and contract data for FY24 and FY25.")

# st.markdown("---")

# st.header("🔗 Quick Navigation")

# st.markdown("""
# - [📊 **Agency Performance Dashboard**](./Agency_Performance_Dashboard)
#     - View detailed performance by agency, program, and metric.
# - [🧾 **Agency Program Summary**](./Agency_Program_Summary)
#     - Compare program performance and trends across years.
# - [📄 **Contract Overview**](./Contract_Overview)
#     - Explore contracts by year, duration, and see target changes.
# - [📚 **Metrics Glossary**](./Metrics_Glossary)
#     - Understand key metrics, definitions, and categories used.
# - [📈 **Metric Trends (FY24–FY25)**](./Metric_Trends_(FY24_vs_FY25))
#     - Compare program performance and trends across years.
# - [🧭 **Program Explorer by Category**](./Program_Explorer_by_Category)
#     - Compare program performance and trends across years.
            
# """)

# st.markdown("---")

# st.info("💡 Tip: Use filters on each page to narrow results by fiscal year, program, or metric type.")


############







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
