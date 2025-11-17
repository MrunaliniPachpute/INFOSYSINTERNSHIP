import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\mruna\Desktop\InfosysInternship\Indian_Traffic_Violations.csv")
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe())
# rows , cols = df.shape
# print("rows", rows)
# print("cols" , cols)

#WHY ONLY THIS DATASET?->TAKE MEDIUM TO LARGE RANGE OF DATASET...AS WHILE TESTING MODEL OR DURING TRAINING N MANIPULATING NOT TO COMPROMIZE WITH ACCURACY SCORE...1)TRAFFIC VIOLATION IS PROBLEM THAT AFFECT PUBLIC SAFTEY...IT HELP UNDERTAND MOST COMMON VIOLATION WEATER, SEATBELT, PAYMENT METHODS AS SEEN IN DATASET...IT CAN PREDICT WEATHER A FINE WILL BE PAYED OR NOT...FINE AMT IS TARGET VALUE...EG IF SUCH VIOLATIONS HAPPEN REGULARLY CHECKING...
#violation id, date ,time fine amt , violation type, payment method, weather condition , drivers age, helmet worn , seat belt worn , court appearance required , fine payed, ]

# print(df['Violation_Type].unique)
# print(df['freq'].count)

speed_record = df[df['Recorded_Speed'] > df['Speed_Limit']]
count = len(speed_record)
total = len(df)

percent = (count / total) * 100

print( count)
print(percent)

#Weather conditions impact on violations
plt.figure(figsize=(12,6))
sns.countplot(
  y='Weather_Condition',
  data=df,
  order=df['Weather_Condition'].value_counts().index,
  palette='magma'
)
plt.tight_layout()
plt.show()

# hw
rainy_df = df[df['Weather_Condition'].str.lower() == 'rainy']
speeding_rainy = rainy_df[rainy_df['Recorded_Speed'] > rainy_df['Speed_Limit']]
count_speeding_rainy = len(speeding_rainy)
total_rainy = len(rainy_df)

# Compute proportion / percentage
percent_speeding_rainy = (count_speeding_rainy / total_rainy) * 100

print("Total violations on rainy days:", total_rainy)
print("Speeding violations on rainy days:", count_speeding_rainy)
print("Percentage of speeding violations on rainy days: {:.2f}%".format(percent_speeding_rainy))
