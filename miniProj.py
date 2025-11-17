import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# tips = sns.load_dataset("tips")

#Which day has heighest tips?
# sns.barplot(x="day" , y="tip" , data=tips)
# plt.title("Average tip by day")
# plt.show()

#Tips by gender and time(Lunch/dinner)
# sns.boxplot(x="time", y="tip", hue="sex",  data=tips)
# plt.title("Tips by gender and time")
# plt.show()

#heatmep
# sns.heatmap(tips.corr(numeric_only=True), annot=True)
# plt.title("overall correlation summary")
# plt.show()

#barplot ->comparing sales of 5 prods

# data = {
#     "Product": ["A", "B", "C", "D", "E"],
#     "Sales": [250, 400, 320, 150, 500]
# }

# df = pd.DataFrame(data)

# sns.barplot(x="Sales", y="Product", data=df)
# plt.title("BARPLOT")
# plt.show()

x = [1, 2, 3, 4, 5]
y_increase = [10, 20, 30, 40, 50]
y_decrease = [50, 40, 30, 20, 10]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# First subplot – increasing trend
axes[0].plot(x, y_increase, marker='o', color='green')
axes[0].set_title("Increasing Trend")
axes[0].set_xlabel("X-axis")
axes[0].set_ylabel("Y-axis")

# Second subplot – decreasing trend
axes[1].plot(x, y_decrease, marker='o', color='red')
axes[1].set_title("Decreasing Trend")
axes[1].set_xlabel("X-axis")
axes[1].set_ylabel("Y-axis")

# Adjust layout
plt.tight_layout()
plt.show()


