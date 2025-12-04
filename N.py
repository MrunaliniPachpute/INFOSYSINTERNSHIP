import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Indian_Traffic_Violations.csv")

# Calculate mean penalty points
avg_risk = df.groupby("Vehicle_Type")["Penalty_Points"].mean().sort_values()

# Convert to DataFrame for seaborn
plot_df = avg_risk.reset_index()
plot_df.columns = ["Vehicle_Type", "Avg_Penalty_Points"]

pro_colors = [
    "#A4278D",
    "#5A5A68",
    "#7BC82F",
    "#8175B7",
    "#CC8724",
    "#6485D0"
]

plt.figure(figsize=(8,5))
sns.barplot(
    data=plot_df,
    x="Avg_Penalty_Points",
    y="Vehicle_Type",
    hue="Vehicle_Type",   # fixes seaborn warning
    palette=pro_colors,
    dodge=False,
    legend=False
)

plt.title("Vehicle Type vs Average Penalty Points", fontsize=14)
plt.xlabel("Average Penalty Points")
plt.ylabel("Vehicle Type")

# Add value labels
for index, row in plot_df.iterrows():
    plt.text(row["Avg_Penalty_Points"] + 0.1, index, f"{row['Avg_Penalty_Points']:.1f}", va="center")

plt.tight_layout()
plt.show()
