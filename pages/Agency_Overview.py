import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agency Overview", layout="wide")
st.title("🏢 Agency Overview by Program and Fiscal Year")

@st.cache_data
def load_data():
    df = pd.read_excel("agency_program_data.xlsx")
    df["Outcome %"] = (df["Actual"] / df["Target"]).replace([float("inf"), -float("inf")], 0) * 100
    return df.drop_duplicates(subset=["Agency ID", "Program Name", "Fiscal Year", "Contract Duration"])

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter")
fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
selected_fy = st.sidebar.multiselect("Fiscal Year", ["All"] + fiscal_years, default="All")
agency_names = sorted(df["Agency Name"].dropna().unique())
selected_agencies = st.sidebar.multiselect("Agency Name", agency_names, default=agency_names)

# --- Filter Data ---
filtered_df = df.copy()
if "All" not in selected_fy:
    filtered_df = filtered_df[filtered_df["Fiscal Year"].isin(selected_fy)]
filtered_df = filtered_df[filtered_df["Agency Name"].isin(selected_agencies)]

# --- Display ---
if filtered_df.empty:
    st.warning("No data matches the current filters.")
else:
    for agency_name in sorted(filtered_df["Agency Name"].unique()):
        agency_df = filtered_df[filtered_df["Agency Name"] == agency_name]

        with st.expander(f"🏢 {agency_name}", expanded=False):
            fiscal_years = sorted(agency_df["Fiscal Year"].unique())

            for fy in fiscal_years:
                st.markdown(f"### 📅 Fiscal Year: {fy}")
                fy_df = agency_df[agency_df["Fiscal Year"] == fy]

                contract_count = fy_df["Program Name"].nunique()
                durations = fy_df["Contract Duration"].value_counts().to_dict()
                duration_summary = ", ".join([f"{v} × {k}" for k, v in durations.items()])
                st.markdown(f"- **Programs:** {contract_count}")
                st.markdown(f"- **Contract Durations:** {duration_summary}")

                for _, row in fy_df.iterrows():
                    st.markdown(f"#### 🏷️ {row['Program Name']} ({row['Contract Duration']})")
                    st.markdown(f"""
                    - 🧩 **Service Category:** {row['Service Category']}
                    - 📂 **Program Type:** {row['Program Type']}
                    - 🕒 **Contract Duration:** {row['Contract Duration']}
                    """)

                    metric_df = df[
                        (df["Agency ID"] == row["Agency ID"]) &
                        (df["Program Name"] == row["Program Name"]) &
                        (df["Fiscal Year"] == row["Fiscal Year"])
                    ]

                    for _, m in metric_df.iterrows():
                        st.markdown(f"""
                        > - **{m['Metric Type']}**  
                        >   🎯 Target: `{int(m['Target'])}`  
                        >   ✅ Actual: `{int(m['Actual'])}`  
                        >   📈 Outcome %: **{m['Outcome %']:.1f}%**
                        """)
                st.markdown("---")
