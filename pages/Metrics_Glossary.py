import streamlit as st

st.set_page_config(page_title="Metric Glossary", layout="wide")
st.title("📚 Metric Glossary & Service Category Guide")

st.markdown("""
This page explains each **service category** and how related **metrics** are defined and interpreted in dashboards and reports.
""")

# -------------------
st.header("🧩 Service Categories")

st.markdown("""
Understanding the **purpose** of each service category helps clarify why certain metrics apply differently.

- **Outreach and Navigation (ON)**  
  Connects families with early childhood resources. Focuses on **referrals** rather than repeated services.  
  → Metric focus: *Individuals Served* (referred).

- **Early Learning (EL)**  
  Supports early development through structured programming and caregiver learning.  
  → Metric focus: *Encounters* (sessions), sometimes duplicated Individuals Served in Play & Learn.

- **Healthy Development (HD)**  
  Ensures access to physical and emotional health services for children and caregivers.  
  → Metric focus: *1:1 or group Encounters*, *Individuals Served*.

- **Parent Education and Support (PES)**  
  Provides home and community-based parenting support and education.  
  → Metric focus: *Encounters*, *Individuals Served*.
""")

# -------------------
st.header("📏 Metric Type Definitions")

with st.expander("🔹Individuals Served (IS)"):
    st.markdown("""
    Represents the **number of distinct individuals** served by a program.

    - Used across ON, HD, PES, and some EL programs.
    - In **Play and Learn**, this may be duplicated (attendees can be counted more than once).

    > Helps measure broad reach — each individual only counted once per program and fiscal year.
    """)

with st.expander("🔹 Encounters"):
    st.markdown("""
    Measures **how often** services were delivered.

    - In PES & HD: Typically *1:1 visits* or sessions.
    - In EL: *Play & Learn sessions*, *group classes*, or *family activities*.
    - In ON: Not always reported.

    > Encounters help capture frequency and intensity of services.
    """)

with st.expander("🔹 Target / Actual / Outcome"):
    st.markdown("""
    - **Target**: Set in contract (e.g., “We will serve 50 individuals”).
    - **Actual**: What the provider actually reports.
    - **Outcome**: Calculated as `Actual / Target × 100`

    > Targets are **contractual goals**. Outcomes indicate progress toward these goals.
    """)

# -------------------
st.header("📊 Core Metric Concepts")

with st.expander("🎯 Target Setting"):
    st.markdown("""
    All targets are set during the **contract negotiation process** between the agency and First Steps Kent.  
    Each program may set targets for:
    - Individuals Served
    - Encounters

    > Dashboards reflect these targets in reporting comparisons.
    """)

with st.expander("📎 Duplicated vs Unduplicated Counts"):
    st.markdown("""
    - **Unduplicated**: Each person counted only once per program — ideal for unique reach.
    - **Duplicated**: People counted multiple times — used in attendance-based programs like Play & Learn.

    > The dashboards will indicate which type of count is used for each metric.
    """)


# -------------------
st.header("🧩 Service Categories Information")
with st.expander("Information"):
    st.markdown("""
    - **Outreach and Navigation**  
    Providers connect expectant parents and families of young children to early childhood information, programming, and community resources to help foster a healthy, safe, and nurturing environment.

    - **Early Learning**  
    Programming supports children’s cognitive, social, and emotional development while increasing parents’ and other adult caregivers’ knowledge and skills in supporting children’s early learning development.

    - **Healthy Development**  
    Providers ensure expectant parents and those with young children have access to comprehensive and coordinated care that optimizes physical and emotional health. Programming follows evidence-based practices that demonstrate success in supporting positive health behaviors for expectant mothers and children.

    - **Parent Education and Support**  
    Services ensure parents have the knowledge and skills to support their children’s health, development, and learning. PE programs provide in-home and/or community-based support and education. In-home services involve trained providers visiting families’ homes to offer one-on-one education and support.
    """)



# -------------------
st.markdown("---")
st.markdown("📎 [Visit First Steps Kent Provider Page](https://www.firststepskent.org/millage/providers) for more details.")
