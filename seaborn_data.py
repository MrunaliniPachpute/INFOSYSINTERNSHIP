import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

#Scater plot
# sns.scatterplot(x="total_bill" , y="tip", data=tips)
#plt.show()

#Adding colors using hue
# sns.scatterplot(x="total_bill" , y="tip" , hue="sex", data=tips)
# plt.title("Tip amount by gender")
# plt.show()

#BARPLOT - avg comparison - center line on bar->median tip
# sns.barplot(x="day" , y="total_bill" , data=tips)
# plt.title("Average total bill per day")
# plt.show()

#Box plot
# sns.boxplot(x="day", y="tip" , data=tips)
# plt.title("Distribution of tips by day")
# plt.show() 

#violin plot //combines boxplot and(kernel density plot(kde)) density curve , shows median and quartile,  used to see whether its symmetric, squid etc n get more info than boxplot
# sns.violinplot(x="day" , y="total_bill" , data=tips)
# plt.title("Bill distribution by day (violin plot)")
# plt.show()

#count plot
# sns.countplot(x='day',  data=tips)
# plt.title("Number of customers per day:count plot")
# plt.show()

#historgam and kde plot
#hist -> shows distribution of only 1 variable
# sns.histplot(tips["total_bill"] , bins=9, kde=True)
# plt.title("Distribution of total bills")
# plt.show()

#joint plot ->combines scatter n hist plot for deeper analysis ...in real life used in advertisement budget n sales
# sns.jointplot(x="total_bill", y="tip" , kind="reg", data=tips)
# plt.show()

#pair plot
# sns.pairplot(tips, hue="sex")
# plt.show()

#heat map - coreelation
# corr = tips.corr(numeric_only=True)
# sns.heatmap(corr , annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

#styling and themes
# sns.set_style("darkgrid")
# sns.barplot(x="day" , y="total_bill" , data=tips)
# plt.title("Styling and themes barplot")
# plt.show()

#Custom color pallet
# sns.color_palette("Set2")
# sns.barplot(x="day", y="tip", hue="sex",  data=tips)
# plt.title("Custom color pallet")
# plt.show()