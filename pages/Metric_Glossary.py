# import streamlit as st

# st.set_page_config(page_title="Metric Glossary", layout="wide")
# st.title("📚 Metric Glossary & Service Category Guide")

# st.markdown("""
# This page helps explain the purpose of each **service category** and how their **metrics** are defined for reporting and evaluation.
# """)

# # -------------------
# st.header("🧩 Service Categories")

# st.markdown("""
# - **Outreach and Navigation**  
#   Providers connect expectant parents and families of young children to early childhood information, programming, and community resources to help foster a healthy, safe, and nurturing environment.

# - **Early Learning**  
#   Programming supports children’s cognitive, social, and emotional development while increasing parents’ and other adult caregivers’ knowledge and skills in supporting children’s early learning development.

# - **Healthy Development**  
#   Providers ensure expectant parents and those with young children have access to comprehensive and coordinated care that optimizes physical and emotional health. Programming follows evidence-based practices that demonstrate success in supporting positive health behaviors for expectant mothers and children.

# - **Parent Education and Support**  
#   Services ensure parents have the knowledge and skills to support their children’s health, development, and learning. PE programs provide in-home and/or community-based support and education. In-home services involve trained providers visiting families’ homes to offer one-on-one education and support.
# """)

# # -------------------
# st.header("📏 Metric Type Definitions")

# with st.expander("**Unique Individuals Served (UIS)**"):
#     st.markdown("""
#     Represents a count of **distinct individuals** served by a program during the reporting period.

#     - In **Outreach & Navigation**: UIS = *number of individuals referred to services* (de-duplicated).
#     - In **Early Learning** (e.g., Play and Learn): UIS = *number of attendees*, which **may include duplicates** if individuals attend multiple sessions.

#     > Always check how UIS is defined for the specific program type.
#     """)

# with st.expander("**Encounters**"):
#     st.markdown("""
#     Measures direct service activities such as home visits, sessions, screenings, or group events.

#     - In **Home Visiting & Parent Education**: Encounters = *in-home or virtual sessions*.
#     - In **Early Learning**: Encounters = *number of play sessions* or *workshops held*.
#     - In **Outreach**: Not always used; programs often report UIS only.

#     > Helps assess frequency and reach of services beyond just the number of individuals served.
#     """)

# with st.expander("**Target / Actual / Outcome**"):
#     st.markdown("""
#     - **Target**: What was planned or contracted for the program to achieve.
#     - **Actual**: What the program reported accomplishing.
#     - **Outcome**: Percent completion of the goal, calculated as  
#       `Actual ÷ Target × 100`

#     > Outcome is only meaningful if the **Target** is set. If Target is 0, the metric is informational only.
#     """)

# # -------------------
# st.markdown("""
# ---
# 📎 [Learn more about First Steps Kent programs](https://www.firststepskent.org/millage/providers)
# """)

import streamlit as st

st.set_page_config(page_title="📖 Metrics Glossary", layout="wide")
st.title("📖 Metrics Glossary")

st.markdown("Use this glossary to better understand the terms and logic used throughout the dashboards. These definitions reflect how metrics are reported and tracked across programs and contracts.")

st.subheader("🧩 Core Metric Definitions")

st.info("All **Targets** listed are based on **contractual expectations** defined by the provider's agreement with First Steps Kent.")

st.markdown("""
- **Unique Individuals Served (Unduplicated Count)**  
  Each individual (child, expectant parent, or caregiver) is counted only once per contract, even if they receive services multiple times. This metric is typically used in Outreach & Navigation and Direct Service programs.

- **Encounters (Duplicated Count)**  
  Total number of times services are delivered, including repeat visits or group sessions. This is commonly used to measure **dosage** or overall activity level.

- **Target**  
  The **projected number** set in the signed contract. This can refer to individuals served or encounters expected, depending on the service category.

- **Actual**  
  The actual number reported by the provider during the contract period.

- **Outcome %**  
  A calculation of progress toward the target:  
  \\\\[
  \\text{Outcome \\%} = \\frac{\\text{Actual}}{\\text{Target}} \\times 100
  \\\\]

- **Dosage**  
  The average number of encounters per individual. Not every contract includes this as a target, but it can be inferred in some cases.
""")

st.subheader("🧭 Service Categories Overview")
with st.expander("Outreach & Navigation"):
    st.markdown("""
    Providers help families connect with services and resources.  
    - **Individuals Served**: Unduplicated  
    - **Encounters**: Not counted — referrals are what matter  
    - **Example Metric**: Number of people referred to services
    """)

with st.expander("Early Learning"):
    st.markdown("""
    Programs support children's development and caregiver education.  
    - **Play & Learn**:  
      - **Individuals Served**: Duplicated (attendees)  
      - **Encounters**: Sessions hosted  
    - **Other EL Programs**: Typically unduplicated individuals and 1:1 encounters
    """)

with st.expander("Healthy Development"):
    st.markdown("""
    Focus on physical and emotional health services.  
    - **Individuals Served**: Typically unduplicated  
    - **Encounters**: Group or 1:1, depending on service
    """)

with st.expander("Parent Education & Support"):
    st.markdown("""
    Supports caregivers with in-home or community-based services.  
    - **Individuals Served**: Unduplicated  
    - **Encounters**: Typically 1:1, direct service encounters
    """)

st.subheader("📌 Notes")
st.markdown("""
- If both **Encounters** and **Individuals Served** are reported, they are shown as separate metrics with their own targets and outcomes.
- You may see duplicated counts used in Play & Learn because sessions are drop-in and group-based, while 1:1 home visits or case-based programs use unduplicated counts.
""")
