# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="Service Category Explorer", layout="wide")
# st.title("🧭 Program Explorer by Category & Type")

# # --- Load Data ---
# @st.cache_data
# def load_data():
#     return pd.read_excel("agency_program_data.xlsx")

# df = load_data()

# # --- Filter UI ---

# # Service Category
# service_categories = sorted(df["Service Category"].dropna().unique())
# selected_services = st.multiselect("Select Service Category", service_categories, default=service_categories)

# # Program Type (filtered from selected service categories)
# filtered_programs = df[df["Service Category"].isin(selected_services)]["Program Type"].dropna().unique()
# selected_program_types = st.multiselect("Select Program Type", sorted(filtered_programs), default=sorted(filtered_programs))

# # Fiscal Year (radio or slider style)
# fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
# selected_fy = st.radio("Select Fiscal Year", options=["All"] + fiscal_years)

# # --- Apply Filters ---
# df_filtered = df[
#     df["Service Category"].isin(selected_services) &
#     df["Program Type"].isin(selected_program_types)
# ]

# if selected_fy != "All":
#     df_filtered = df_filtered[df_filtered["Fiscal Year"] == selected_fy]


# # --- Group by Program and Show Metrics ---
# if df_filtered.empty:
#     st.warning("No programs match your filters.")
# else:
#     for (program_type), df_type in df_filtered.groupby("Program Type"):
#         with st.expander(f"📘 {program_type}", expanded=True):
#             grouped = df_type.groupby(["Agency ID", "Program Name", "Metric Type"]).agg({
#                 "Target": "sum",
#                 "Actual": "sum"
#             }).reset_index()

#             for (agency_id, program_name), group_df in grouped.groupby(["Agency ID", "Program Name"]):
#                 st.markdown(f"### 🏷️ **{program_name}** ({agency_id})")
#                 for _, row in group_df.iterrows():
#                     metric = row["Metric Type"]
#                     target = int(row["Target"])
#                     actual = int(row["Actual"])
#                     outcome_pct = (actual / target) * 100 if target > 0 else 0

#                     st.markdown(f"""
#                     - **{metric}**  
#                       🎯 Target: `{target}`  
#                       ✅ Actual: `{actual}`  
#                       📈 Outcome: **{outcome_pct:.1f}%**
#                     """)


import streamlit as st
import pandas as pd

st.set_page_config(page_title="Service Category Explorer", layout="wide")
st.title("🧭 Explore Programs by Service Category")

# --- Load Excel Data ---
@st.cache_data
def load_data():
    return pd.read_excel("agency_program_data.xlsx")

df = load_data()

# --- Filter UI ---
st.sidebar.header("🔎 Filter")

# Service Category
all_services = sorted(df["Service Category"].dropna().unique())
selected_services = st.sidebar.multiselect("Service Category", all_services, default=all_services)

# Program Types based on selected service categories
programs_filtered = df[df["Service Category"].isin(selected_services)]
all_types = sorted(programs_filtered["Program Type"].dropna().unique())
selected_types = st.sidebar.multiselect("Program Type", all_types, default=all_types)

# Fiscal Year
fiscal_years = sorted(df["Fiscal Year"].dropna().unique())
selected_fy = st.sidebar.radio("Fiscal Year", options=["All"] + fiscal_years)

# --- Apply Filters ---
df_filtered = df[
    df["Service Category"].isin(selected_services) &
    df["Program Type"].isin(selected_types)
]

if selected_fy != "All":
    df_filtered = df_filtered[df_filtered["Fiscal Year"] == selected_fy]

# --- Show Output ---
if df_filtered.empty:
    st.warning("No programs match your filters.")
else:
    for program_type in sorted(df_filtered["Program Type"].unique()):
        with st.expander(f"📘 {program_type}", expanded=True):
            df_type = df_filtered[df_filtered["Program Type"] == program_type]

            grouped = df_type.groupby(["Agency ID", "Program Name", "Metric Type"]).agg({
                "Target": "sum",
                "Actual": "sum"
            }).reset_index()

            for (agency_id, program_name), group_df in grouped.groupby(["Agency ID", "Program Name"]):
                st.markdown(f"### 🏷️ **{program_name}** ({agency_id})")
                for _, row in group_df.iterrows():
                    metric = row["Metric Type"]
                    target = int(row["Target"])
                    actual = int(row["Actual"])
                    pct = (actual / target) * 100 if target > 0 else 0

                    st.markdown(f"""
                    - **{metric}**  
                      🎯 Target: `{target}`  
                      ✅ Actual: `{actual}`  
                      📈 Outcome: **{pct:.1f}%**
                    """)

