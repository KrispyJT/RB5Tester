import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="📊 Agency Metric Comparison", layout="wide")
st.title("📊 Metric Comparison by Fiscal Year")

@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# --- Top-Level Filters ---
st.markdown("### 🔍 Select an Agency and Program")
col1, col2 = st.columns(2)
with col1:
    agencies = sorted(df["Agency Name"].dropna().unique())
    selected_agency = st.selectbox("Agency", agencies)

with col2:
    programs = sorted(df[df["Agency Name"] == selected_agency]["Program Name"].dropna().unique())
    selected_program = st.selectbox("Program", programs)

df_filtered = df[(df["Agency Name"] == selected_agency) & (df["Program Name"] == selected_program)]

if df_filtered.empty:
    st.warning("No data found for the selected agency and program.")
    st.stop()

metric_types = df_filtered["Metric Type"].dropna().unique()
st.markdown(f"### 📊 Viewing Data for: **{selected_program}** at **{selected_agency}**")


# --- Target vs Actual FIRST ---
st.subheader("📊 Target vs Actual Comparison by Metric")
target_actual_cols = st.columns(len(metric_types))

for i, metric in enumerate(metric_types):
    metric_df = df_filtered[df_filtered["Metric Type"] == metric]
    grouped = metric_df.groupby("Fiscal Year")[["Target", "Actual"]].sum().reset_index()
    melted = grouped.melt(id_vars="Fiscal Year", value_vars=["Target", "Actual"],
                          var_name="Metric", value_name="Value")

    fig_compare = px.bar(
        melted,
        x="Fiscal Year",
        y="Value",
        color="Metric",
        barmode="group",
        title=f"{metric} — Target vs Actual by Year",
        text="Value",
        labels={"Value": "Count"},
    )
    fig_compare.update_traces(textposition="outside")
    target_actual_cols[i].plotly_chart(fig_compare, use_container_width=True)


# --- Outcome % Comparison (Line Chart) ---
st.subheader("📈 Outcome % by Metric Type (Line Chart)")

line_df = pd.DataFrame()

# Build a combined DataFrame for all metrics
for metric in metric_types:
    metric_df = df_filtered[df_filtered["Metric Type"] == metric]
    grouped = metric_df.groupby("Fiscal Year")[["Target", "Actual"]].sum().reset_index()
    grouped["Outcome %"] = grouped.apply(lambda row: (row["Actual"] / row["Target"] * 100) if row["Target"] > 0 else 0, axis=1)
    grouped["Metric Type"] = metric
    line_df = pd.concat([line_df, grouped[["Fiscal Year", "Outcome %", "Metric Type"]]])

# Line chart
fig_line = px.line(
    line_df,
    x="Fiscal Year",
    y="Outcome %",
    color="Metric Type",
    markers=True,
    title="Outcome % by Metric Type (FY Comparison)",
    labels={"Outcome %": "Outcome Percentage"},
)

fig_line.update_traces(mode="lines+markers")
fig_line.update_layout(yaxis=dict(range=[0, max(120, line_df["Outcome %"].max() + 10)]))
st.plotly_chart(fig_line, use_container_width=True)


# --- Actuals by Metric Type ---
# st.subheader("📊 Actuals by Metric Type and Fiscal Year")
# actual_cols = st.columns(len(metric_types))

# for i, metric in enumerate(metric_types):
#     metric_df = df_filtered[df_filtered["Metric Type"] == metric]
#     grouped = metric_df.groupby("Fiscal Year")[["Actual"]].sum().reset_index()

#     fig_actual = px.bar(
#         grouped,
#         x="Fiscal Year",
#         y="Actual",
#         text=grouped["Actual"],
#         color="Fiscal Year",
#         title=f"{metric} — Actuals by Year",
#         labels={"Actual": "Actual"},
#     )
#     fig_actual.update_traces(textposition="outside")
#     fig_actual.update_layout(yaxis=dict(range=[0, grouped["Actual"].max() + 20]))
#     actual_cols[i].plotly_chart(fig_actual, use_container_width=True)


# --- Optional Data Table ---
with st.expander("🔍 View Raw Data"):
    st.dataframe(df_filtered.sort_values(by="Fiscal Year"))
