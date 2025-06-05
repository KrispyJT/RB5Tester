import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📊 Agency Metric Comparison", layout="wide")
st.title("📊 Metric Comparison by Fiscal Year")

@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
agencies = sorted(df["Agency Name"].dropna().unique())
selected_agency = st.sidebar.selectbox("Select Agency", agencies)

# Filter programs based on agency
programs = sorted(df[df["Agency Name"] == selected_agency]["Program Name"].dropna().unique())
selected_program = st.sidebar.selectbox("Select Program", programs)

# Filter for agency/program
df_filtered = df[(df["Agency Name"] == selected_agency) & (df["Program Name"] == selected_program)]

if df_filtered.empty:
    st.warning("No data found for the selected agency and program.")
    st.stop()

# --- Group by Fiscal Year & Metric Type ---
st.subheader(f"📈 Outcome Comparison for: {selected_program} ({selected_agency})")
metric_types = df_filtered["Metric Type"].dropna().unique()

cols = st.columns(len(metric_types))

for i, metric in enumerate(metric_types):
    metric_df = df_filtered[df_filtered["Metric Type"] == metric]
    grouped = metric_df.groupby("Fiscal Year")[["Target", "Actual"]].sum().reset_index()
    grouped["Outcome %"] = grouped.apply(lambda row: (row["Actual"] / row["Target"] * 100) if row["Target"] > 0 else 0, axis=1)

    fig = px.bar(
        grouped,
        x="Fiscal Year",
        y="Outcome %",
        text=grouped["Outcome %"].apply(lambda x: f"{x:.1f}%"),
        color="Fiscal Year",
        title=metric,
        labels={"Outcome %": "Outcome %"},
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(yaxis=dict(range=[0, max(120, grouped["Outcome %"].max() + 20)]))

    cols[i].plotly_chart(fig, use_container_width=True)


# --- Actuals Comparison Chart ---
st.subheader("📊 Actuals by Metric and Year")
actual_cols = st.columns(len(metric_types))

for i, metric in enumerate(metric_types):
    metric_df = df_filtered[df_filtered["Metric Type"] == metric]
    grouped = metric_df.groupby("Fiscal Year")[["Actual"]].sum().reset_index()

    fig_actual = px.bar(
        grouped,
        x="Fiscal Year",
        y="Actual",
        text=grouped["Actual"],
        color="Fiscal Year",
        title=f"{metric} — Actuals by Year",
        labels={"Actual": "Actual"},
    )
    fig_actual.update_traces(textposition="outside")
    fig_actual.update_layout(yaxis=dict(range=[0, grouped["Actual"].max() + 20]))

    actual_cols[i].plotly_chart(fig_actual, use_container_width=True)




# --- Combined Target vs Actual Chart ---
st.subheader("📊 Target vs Actual Comparison")
target_actual_cols = st.columns(len(metric_types))

for i, metric in enumerate(metric_types):
    metric_df = df_filtered[df_filtered["Metric Type"] == metric]
    grouped = metric_df.groupby("Fiscal Year")[["Target", "Actual"]].sum().reset_index()
    melted = grouped.melt(id_vars="Fiscal Year", value_vars=["Target", "Actual"], var_name="Metric", value_name="Value")

    fig_compare = px.bar(
        melted,
        x="Fiscal Year",
        y="Value",
        color="Metric",
        barmode="group",
        title=f"{metric} — Target vs Actual by Year",
        text="Value",
        labels={"Value": "Count"}
    )
    fig_compare.update_traces(textposition="outside")
    target_actual_cols[i].plotly_chart(fig_compare, use_container_width=True)

# --- Raw Table ---
with st.expander("🔍 View Underlying Data"):
    st.dataframe(df_filtered.sort_values(by="Fiscal Year"))
