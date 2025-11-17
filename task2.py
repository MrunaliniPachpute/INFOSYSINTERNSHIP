import pandas as pd
import numpy as np

# Employee data
data = {
    "Emp_Name": ["Mrunalini", "Aaru", "Bob", "Charlie", "David"],
    "Base_Salary": [1250000, 1060000, 1455000, 4548000, 6770000],
    "Bonus": [55000, 67000, 36000, 74500, 98000]
}

df = pd.DataFrame(data)
print(df)


df["Total_Salary"] = np.add(df["Base_Salary"], df["Bonus"])

# tax ->30% of total
df["Tax"] = np.multiply(df["Total_Salary"], 0.30)

# net_Sal = tot - Tax
df["Net_Salary"] = np.subtract(df["Total_Salary"], df["Tax"])

print("\nEmployee Salary Report:\n", df)

