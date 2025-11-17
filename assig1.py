import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#create a line plot showing temp over 7 days
# data = {
#   "temp" : [70, 20, 40 , 30 ,10, 2, 8],
#   "day" : [1, 2,3, 4, 5, 6, 7]
# }

# df = pd.DataFrame(data)

# sns.lineplot(x="day" , y="temp" , data = df)
# plt.title("Temp over 7 days")
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.show()

#make a barchart comparing sales of 5 prods
# data = {
#   "product" : ["p1" , "p2" , "p3" , "p4" , "p5"],
#   "sales" : [70, 60, 90, 50, 80]
# }

# df = pd.DataFrame(data)
# sns.barplot(x="product" , y="sales" , data=df)
# plt.xlabel("product")
# plt.ylabel("sales")
# plt.title("Sales of products")
# plt.show()

#create a scatter plot showing height versus weight of 10 students
# data = {
#   "height" : [70, 40, 50, 88, 90, 89, 75, 66, 77, 59],
#   "weight" : [60, 30, 40, 77, 88 , 79, 64, 55, 66, 49]
# }

# df = pd.DataFrame(data)

# sns.scatterplot(x="weight" , y="height" , color="red" , marker="*",  data=df)
# plt.title("Height versus weight of students")
# plt.xlabel("Height (in cm or inches)") 
# plt.ylabel("Weight (in kg)")     
# plt.show()

#draw a pie chart showing time spend on 4 daily activisties
# data = {
#   "time" : [4, 3, 5, 2],
#   "activity" : ["study" , "rest" , "school" , "play"]
# }

# df = pd.DataFrame(data)

# plt.pie(df["time"] , labels=df["activity"], autopct="%1.1f%%", startangle=0)
# plt.title("Time Spent on Daily Activities")
# plt.show()

#combine 2 line graphs inc n dec using subplots
# data1 = {
#     "day": [1, 3, 5, 7,9],
#     "sales_inc": [10, 20, 30, 40, 50]
# }

# data2 = {
#     "day": [2, 4, 6, 8,10],
#     "sales_dec": [50, 40, 30, 20, 10]
# }

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# sns.lineplot( x=df1["day"][::1], y=df1["sales_inc"][::1],color="green" ,marker='o', label="increasing")

# sns.lineplot( x=df2["day"][::1], y=df2["sales_dec"][::1], color="red" ,marker='o', label="decreasing")

# plt.title("Inc v/s Dec Sales")
# plt.xlabel("Day")
# plt.ylabel("Sales")


# plt.legend()
# plt.show()


#display multipel trends using diff colors n markers
data = {
    "day": [1, 2, 3, 4, 5],
    "A": [10, 20, 25, 30, 40],
    "B": [5, 15, 20, 35, 45],
    "C": [2, 8, 18, 28, 38]
}

df = pd.DataFrame(data)

sns.lineplot(x="day", y="A", data=df, color="green", marker='o', label="Product A")

sns.lineplot(x="day", y="B", data=df, color="blue", marker='s', label="Product B")

sns.lineplot(x="day", y="C", data=df, color="orange", marker='^', label="Product C")

plt.title("Multiple Sales Trends")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.show()