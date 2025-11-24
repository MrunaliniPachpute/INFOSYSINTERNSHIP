import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown(
    """
    <h1 style="
        background: linear-gradient(to right, #ff512f, #dd2476);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
        font-size: 48px;
        font-weight: bold;
    ">
    Smart Traffic Violation Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(to right, #ff512f, #dd2476);
        color: white;
        padding: 10px 22px;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)


data = st.file_uploader("Upload your traffic dataset", type=["csv"])

if data:
    df = pd.read_csv(data)
    st.subheader("Data Preview")
    st.dataframe(df)

    # SEVERITY SCORE CALCULATION
    def calc_severity_score(row):
        severity = 0

        if pd.notnull(row.get('Fine_Amount')):
            severity += row['Fine_Amount'] / 1000

        severity += row.get('Penalty_Points', 0)

        if pd.notnull(row.get('Recorded_Speed')) and pd.notnull(row.get('Speed_Limit')):
            overspeed = row['Recorded_Speed'] - row['Speed_Limit']
            if overspeed > 0:
                severity += overspeed / 10

        if pd.notnull(row.get('Alcohol_Level')):
            severity += row['Alcohol_Level'] * 10

        if row.get('Helmet_Worn') == 'No':
            severity += 10
        if row.get('Seatbelt_Worn') == 'No':
            severity += 10

        if row.get('Traffic_Light_Status') == 'Red':
            severity += 15

        severity += row.get('Previous_Violations', 0) * 1.5

        return severity

    df['Violation_Severity_Score'] = df.apply(calc_severity_score, axis=1)

    st.sidebar.title("Filters")
    violation_types = df['Violation_Type'].unique()
    chosen_type = st.sidebar.selectbox("Select Violation Type", violation_types)

    #new df
    df_filtered = df[df['Violation_Type'] == chosen_type]

    #counting location wise no of violations acc to chosen violation type
    violations = df_filtered.groupby("Location").size().reset_index(name="Violation_Count")
    violations["Location"] = violations["Location"].str.strip().str.title()

    path = r"C:\\Users\\mruna\\Desktop\\InfosysInternship\\India-State-and-Country-Shapefile-Updated-Jan-2020-master\\India-State-and-Country-Shapefile-Updated-Jan-2020-master\\India_State_Boundary.shp"
    states = gpd.read_file(path)
    states["State_Name"] = states["State_Name"].str.strip().str.title()

    merged = states.merge(
        violations,
        left_on="State_Name",
        right_on="Location",
        how="left"
    )

    st.subheader("Violation Count Map by State")

    fig1, ax1 = plt.subplots(1, 1, figsize=(17, 7))

    merged.plot(
        column="Violation_Count",
        cmap="Reds",
        legend=True,
        edgecolor="black",
        linewidth=0.5,
        missing_kwds={"color": "lightgrey", "label": "No Data"},
        ax=ax1
    )

    plt.title(f"Violations in India for '{chosen_type}'", fontsize=20)
    plt.axis("off")
    st.pyplot(fig1, use_container_width=False)

    if data and st.button("View Filtered data "):
      st.subheader(f"Filtered Data for: {chosen_type}")
      #df_filtered
      st.dataframe(violations)


    #heatmap
    st.subheader("Average Severity Heatmap")
    
    location_heatmap = df.pivot_table(
        values='Violation_Severity_Score',
        index='Location',
        columns='Violation_Type',
        aggfunc=np.mean
    )

    fig2 = plt.figure(figsize=(14, 7))
    sns.heatmap(location_heatmap, cmap='coolwarm', annot=True)
    plt.title("Average Severity Score by Location and Violation Type")
    plt.tight_layout()

    st.pyplot(fig2)

if data and st.button("Get Summary Stats of heatmap"):
    st.subheader("Summary Statistics")
    st.write(location_heatmap.describe())

