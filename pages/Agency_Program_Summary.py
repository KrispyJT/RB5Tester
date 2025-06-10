



import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agency Overview", layout="wide")
st.title("🏢 Agency Overview by Program and Fiscal Year")

@st.cache_data
def load_data():
    df = pd.read_excel("agency_program_data.xlsx")
    df["Outcome %"] = (df["Actual"] / df["Target"]).replace([float("inf"), -float("inf")], 0) * 100
    return df

df = load_data()
st.info("Click each section below to expand and learn more about agencies.")
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
                durations = fy_df[["Program Name", "Contract Duration"]].drop_duplicates()["Contract Duration"].value_counts().to_dict()
                duration_summary = ", ".join([f"{v} × {k}" for k, v in durations.items()])
                st.markdown(f"- **Programs:** {contract_count}")
                st.markdown(f"- **Contract Durations:** {duration_summary}")

                for program_name in sorted(fy_df["Program Name"].unique()):
                    program_df = fy_df[fy_df["Program Name"] == program_name]
                    contract_duration = program_df["Contract Duration"].iloc[0]
                    service_category = program_df["Service Category"].iloc[0]
                    program_type = program_df["Program Type"].iloc[0]

                    st.markdown(f"#### 🏷️ {program_name} ({contract_duration})")
                    st.markdown(f"""
                    - 🧩 **Service Category:** {service_category}  
                    - 📂 **Program Type:** {program_type}  
                    - 🕒 **Contract Duration:** {contract_duration}
                    """)

                    for _, row in program_df.iterrows():
                        metric = row["Metric Type"]
                        target = int(row["Target"])
                        actual = int(row["Actual"])
                        outcome = row["Outcome %"]
                        st.markdown(f"""
                        > - **{metric}**  
                        >   🎯 Target: `{target}`  
                        >   ✅ Actual: `{actual}`  
                        >   📈 Outcome %: **{outcome:.1f}%**
                        """)
                st.markdown("---")





# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="Agency Overview", layout="wide")
# st.title("🏢 Agency Overview by Program and Fiscal Year")

# @st.cache_data
# def load_data():
#     df = pd.read_excel("agency_program_data.xlsx")
#     df["Outcome %"] = (df["Actual"] / df["Target"]).replace([float("inf"), -float("inf")], 0) * 100
#     return df

# df = load_data()

# # --- Inline Filters ---
# st.subheader("🔎 Filter Programs")

# fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
# selected_fy = st.multiselect("Fiscal Year", ["All"] + fiscal_years, default="All")

# agency_names = sorted(df["Agency Name"].dropna().unique())
# selected_agencies = st.multiselect("Agency Name", agency_names, default=agency_names)

# # --- Filter Data ---
# filtered_df = df.copy()
# if "All" not in selected_fy:
#     filtered_df = filtered_df[filtered_df["Fiscal Year"].isin(selected_fy)]
# filtered_df = filtered_df[filtered_df["Agency Name"].isin(selected_agencies)]

# # --- Display ---
# if filtered_df.empty:
#     st.warning("No data matches the current filters.")
# else:
#     for agency_name in sorted(filtered_df["Agency Name"].unique()):
#         agency_df = filtered_df[filtered_df["Agency Name"] == agency_name]

#         with st.expander(f"🏢 {agency_name}", expanded=False):
#             fiscal_years = sorted(agency_df["Fiscal Year"].unique())

#             for fy in fiscal_years:
#                 st.markdown(f"### 📅 Fiscal Year: {fy}")
#                 fy_df = agency_df[agency_df["Fiscal Year"] == fy]

#                 contract_count = fy_df["Program Name"].nunique()
#                 durations = fy_df[["Program Name", "Contract Duration"]].drop_duplicates()["Contract Duration"].value_counts().to_dict()
#                 duration_summary = ", ".join([f"{v} × {k}" for k, v in durations.items()])
#                 st.markdown(f"- **Programs:** {contract_count}")
#                 st.markdown(f"- **Contract Durations:** {duration_summary}")

#                 for program_name in sorted(fy_df["Program Name"].unique()):
#                     program_df = fy_df[fy_df["Program Name"] == program_name]
#                     contract_duration = program_df["Contract Duration"].iloc[0]
#                     service_category = program_df["Service Category"].iloc[0]
#                     program_type = program_df["Program Type"].iloc[0]

#                     st.markdown(f"#### 🏷️ {program_name} ({contract_duration})")
#                     st.markdown(f"""
#                     - 🧩 **Service Category:** {service_category}  
#                     - 📂 **Program Type:** {program_type}  
#                     - 🕒 **Contract Duration:** {contract_duration}
#                     """)

#                     for _, row in program_df.iterrows():
#                         metric = row["Metric Type"]
#                         target = int(row["Target"])
#                         actual = int(row["Actual"])
#                         outcome = row["Outcome %"]
#                         st.markdown(f"""
#                         > - **{metric}**  
#                         >   🎯 Target: `{target}`  
#                         >   ✅ Actual: `{actual}`  
#                         >   📈 Outcome %: **{outcome:.1f}%**
#                         """)
#                 st.markdown("---")
