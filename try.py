import pandas as pd
df=pd.read_csv(r"C:\Users\mruna\Desktop\InfosysInternship\Indian_Traffic_Violations.csv")
print(df.columns)
# print(df.info())
# print(df.describe())
# rows , cols = df.shape
# print("rows", rows)
# print("cols" , cols)

#WHY ONLY THIS DATASET?->TAKE MEDIUM TO LARGE RANGE OF DATASET...AS WHILE TESTING MODEL OR DURING TRAINING N MANIPULATING NOT TO COMPROMIZE WITH ACCURACY SCORE...1)TRAFFIC VIOLATION IS PROBLEM THAT AFFECT PUBLIC SAFTEY...IT HELP UNDERTAND MOST COMMON VIOLATION WEATER, SEATBELT, PAYMENT METHODS AS SEEN IN DATASET...IT CAN PREDICT WEATHER A FINE WILL BE PAYED OR NOT...FINE AMT IS TARGET VALUE...EG IF SUCH VIOLATIONS HAPPEN REGULARLY CHECKING...
#violation id, date ,time fine amt , violation type, payment method, weather condition , drivers age, helmet worn , seat belt worn , court appearance required , fine payed, 

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.fillna({'Payment_Method': 'Unknown', 'Weather_Condition': 'Clear'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.hour  # Extract hour
df['Fine_Paid'] = df['Fine_Paid'].map({'Yes':1, 'No':0})  # Convert to numeric
df['Helmet_Worn'] = df['Helmet_Worn'].map({'Yes':1, 'No':0})
df['Seat_Belt_Worn'] = df['Seat_Belt_Worn'].map({'Yes':1, 'No':0})
