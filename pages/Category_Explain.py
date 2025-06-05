import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Set Streamlit config
st.set_page_config(page_title="Service Category Explorer", layout="wide")
st.title("🧭 Explore Programs by Service Category")

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filter")
all_services = sorted(df["Service Category"].dropna().unique())
selected_services = st.sidebar.multiselect("Service Category", all_services, default=all_services)

filtered_programs = df[df["Service Category"].isin(selected_services)]
all_types = sorted(filtered_programs["Program Type"].dropna().unique())
selected_types = st.sidebar.multiselect("Program Type", all_types, default=all_types)

fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
selected_fy = st.sidebar.radio("Fiscal Year", options=["All"] + fiscal_years)

# Filter data based on selection
df_filtered = df[
    df["Service Category"].isin(selected_services) &
    df["Program Type"].isin(selected_types)
]

if selected_fy != "All":
    df_filtered = df_filtered[df_filtered["Fiscal Year"] == selected_fy]

# Display results
if df_filtered.empty:
    st.warning("No programs match your filters.")
else:
    for program_type in sorted(df_filtered["Program Type"].unique()):
        with st.expander(f"📘 {program_type}", expanded=True):
            df_type = df_filtered[df_filtered["Program Type"] == program_type]
            grouped = df_type.groupby(["Agency ID", "Agency Name", "Program Name", "Metric Type"]).agg({
                "Target": "sum",
                "Actual": "sum"
            }).reset_index()

            for (agency_id, agency_name, program_name), group_df in grouped.groupby(["Agency ID", "Agency Name", "Program Name"]):
                st.markdown(f"### 🏷️ **{program_name}**")
                st.markdown(f"📌 Agency: **{agency_name}** ({agency_id})")

                for _, row in group_df.iterrows():
                    metric = row["Metric Type"]
                    target = int(row["Target"])
                    actual = int(row["Actual"])
                    pct = (actual / target) * 100 if target > 0 else 0

                    col1, col2 = st.columns([2, 3])
                    with col1:
                        st.markdown(f"""
                        **{metric}**
                        - 🎯 Target: `{target}`
                        - ✅ Actual: `{actual}`
                        - 📈 Outcome: **{pct:.1f}%**
                        """)
                    with col2:
                        fig = go.Figure(go.Bar(
                            x=[target, actual],
                            y=["Target", "Actual"],
                            orientation='h',
                            marker_color=["#d62728", "#2ca02c"]
                        ))
                        fig.update_layout(height=150, margin=dict(l=30, r=30, t=20, b=20))
                        st.plotly_chart(fig, use_container_width=True)
