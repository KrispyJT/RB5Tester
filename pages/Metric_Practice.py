
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📈 Trends by Metric & Category", layout="wide")
st.title("📈 Metric Trends & Category Analysis")

@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# Filter only FY24 and FY25 for now
df = df[df["Fiscal Year"].isin(["FY24", "FY25"])]

# --- Line Chart: Targets Over Time ---
st.header("📊 Target Trends by Metric Type")

target_df = df.groupby(["Fiscal Year", "Metric Type"])["Target"].sum().reset_index()

fig_line = px.line(
    target_df,
    x="Fiscal Year",
    y="Target",
    color="Metric Type",
    markers=True,
    title="Target Totals by Metric Type (FY24 vs FY25)",
    labels={"Target": "Total Target"},
)
st.plotly_chart(fig_line, use_container_width=True)

# --- Line Chart: Actuals Over Time ---
st.header("📊 Actual Trends by Metric Type")

actual_df = df.groupby(["Fiscal Year", "Metric Type"])["Actual"].sum().reset_index()

fig_actual = px.line(
    actual_df,
    x="Fiscal Year",
    y="Actual",
    color="Metric Type",
    markers=True,
    title="Actual Totals by Metric Type (FY24 vs FY25)",
    labels={"Actual": "Total Actual"},
)
st.plotly_chart(fig_actual, use_container_width=True)

# # --- Line Chart: Targets vs Actuals by Metric ---
# st.header("📉 Target vs Actual by Metric Type")

# comparison_df = df.groupby(["Fiscal Year", "Metric Type"])[["Target", "Actual"]].sum().reset_index()
# melted = comparison_df.melt(id_vars=["Fiscal Year", "Metric Type"], value_vars=["Target", "Actual"],
#                             var_name="Measure", value_name="Count")

# fig_compare = px.line(
#     melted,
#     x="Fiscal Year",
#     y="Count",
#     color="Measure",
#     line_dash="Metric Type",
#     markers=True,
#     title="Target vs Actual by Metric Type (FY24 vs FY25)",
#     labels={"Count": "Total Count"},
#     facet_col="Metric Type",
#     facet_col_wrap=2,
# )
# fig_compare.update_layout(height=600)
# st.plotly_chart(fig_compare, use_container_width=True)

# --- Bar Chart: Actuals by Category, Program, and Metric ---
# st.header("📊 Actuals by Service Category, Program Type, and Metric Type")

# bar_df = df.groupby(["Fiscal Year", "Service Category", "Program Type", "Metric Type"])["Actual"].sum().reset_index()

# fig_bar = px.bar(
#     bar_df,
#     x="Actual",
#     y="Service Category",
#     color="Metric Type",
#     orientation="h",
#     barmode="stack",
#     facet_col="Fiscal Year",
#     title="Actuals by Service Category & Program Type (Split by Metric Type)",
#     labels={"Actual": "Total Actual"},
#     text_auto=True
# )
# fig_bar.update_layout(height=700)
# st.plotly_chart(fig_bar, use_container_width=True)
## Not NEEDED? 





#############
# --- UIS Only ---
st.header("👤 Individuals Served (UIS) — Actuals")
uis_df = df[df["Metric Type"] == "Individuals Served"]
uis_grouped = uis_df.groupby(["Fiscal Year", "Service Category", "Program Type"])["Actual"].sum().reset_index()

fig_uis = px.bar(
    uis_grouped,
    x="Actual",
    y="Service Category",
    color="Program Type",
    orientation="h",
    barmode="stack",
    facet_col="Fiscal Year",
    title="UIS Actuals by Service Category & Program Type (FY24 vs FY25)",
    labels={"Actual": "Total Actual"},
)
st.plotly_chart(fig_uis, use_container_width=True)

# --- Encounters Only ---
st.header("🤝 Encounters — Actuals")
enc_df = df[df["Metric Type"] == "Encounters"]
enc_grouped = enc_df.groupby(["Fiscal Year", "Service Category", "Program Type"])["Actual"].sum().reset_index()

fig_enc = px.bar(
    enc_grouped,
    x="Actual",
    y="Service Category",
    color="Program Type",
    orientation="h",
    barmode="stack",
    facet_col="Fiscal Year",
    title="Encounters Actuals by Service Category & Program Type (FY24 vs FY25)",
    labels={"Actual": "Total Actual"},
)
st.plotly_chart(fig_enc, use_container_width=True)
