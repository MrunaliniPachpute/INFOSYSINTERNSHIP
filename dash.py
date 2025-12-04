import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title("📊 Basic Analytics Dashboard")
st.write("This dashboard shows two simple plots — one using Matplotlib and one using Seaborn.")

np.random.seed(42)
df = pd.DataFrame({
    "Category": np.repeat(["A", "B", "C"], 50),
    "Value": np.random.randint(10, 100, 150),
    "Score": np.random.normal(50, 15, 150)
})

#sidebar 
st.sidebar.title("Filters")
st.sidebar.header("Choose your Category : ")

selected_cat = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

filtered_df = df[df["Category"] == selected_cat]

st.write(f"### Showing Data for Category **{selected_cat}**")
st.dataframe(filtered_df)

# -------------------------------------
# PLOT 1 — MATPLOTLIB
# -------------------------------------
st.subheader("📈 Matplotlib Line Chart")

fig1, ax1 = plt.subplots()
ax1.plot(filtered_df["Value"],marker='o', color="red")
ax1.grid(True) 
ax1.set_facecolor("#f0f0f0") 
ax1.set_title(f"Value Trend for Category {selected_cat}")
ax1.set_xlabel("Index")
ax1.set_ylabel("Value")

st.pyplot(fig1)

# -------------------------------------
# PLOT 2 — SEABORN
# -------------------------------------
st.subheader("📉 Seaborn Distribution Plot")

fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["Score"], kde=True, ax=ax2)
ax2.set_title(f"Score Distribution for Category {selected_cat}")

st.pyplot(fig2)

# -------------------------------------
# FOOTER
# -------------------------------------
st.markdown("---")
st.write("Dashboard built with ❤️ using **Streamlit**, **Matplotlib**, and **Seaborn**.")
