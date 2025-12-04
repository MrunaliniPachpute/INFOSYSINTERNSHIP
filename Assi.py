import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Indian_Traffic_Violations.csv")

#1. CREATE SEVERITY SCORE 
severity_map = {
    "OverSpeeding": 5,
    "Speeding": 5,
    "No Helmet": 4,
    "Triple Riding": 5,
    "Signal Jump": 4,
    "Drunk Driving": 7,
    "No Seatbelt": 3,
    "Wrong Parking": 1
}

df["Severity_Score"] = df["Violation_Type"].map(severity_map).fillna(2)

# Create Vehicle_ID for grouping
df["Vehicle_ID"] = (
    df["Registration_State"].astype(str) + "_" +
    df["Vehicle_Model_Year"].astype(str) + "_" +
    df["Vehicle_Color"].astype(str)
)

# 2. RISK INDEX 
risk_index = df.groupby("Vehicle_ID")["Severity_Score"].sum().sort_values(ascending=False)
print("\nTop 10 Highest Risk Vehicles:")
print(risk_index.head(10))


# 3. MOST COMMON VIOLATION COMBINATIONS

df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

df = df.sort_values(["Vehicle_ID", "DateTime"])

print(df["DateTime"])


df["Next_Violation"] = df.groupby("Vehicle_ID")["Violation_Type"].shift(-1)

df["Violation_Pair"] = df["Violation_Type"] + " → " + df["Next_Violation"]
pairs = df["Violation_Pair"].dropna()

common_pairs = pairs.value_counts().head(10)
print("\nTop 10 Violation Combinations:")
print(common_pairs)


# 4.TOP 5 VIOLATIONS HRS

df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

hour_counts = df["Hour"].value_counts().sort_values(ascending=False)

print("\nTop 5 Time Windows with Maximum Violations:")

for hr, cnt in hour_counts.head(5).items():
    print(f"{hr}:00–{hr}:59 → {cnt} violations")

top5 = hour_counts.head(5)
plt.figure(figsize=(10,5))
sns.barplot(x=top5.index, y=top5.values, color="red")
plt.xlabel("Hour of Day")
plt.ylabel("Violation Count")
plt.title("Top 5 Violation Time Windows")
plt.tight_layout()
plt.show()


# 5.VEHICLES VIOLATING AT LEAST ONCE EVERY WEEK

df["Week"] = pd.to_datetime(df["Date"]).dt.isocalendar().week
df["Year"] = pd.to_datetime(df["Date"]).dt.year

weekly = df.groupby(["Vehicle_ID", "Year", "Week"]).size().reset_index(name="Count")

all_weeks = weekly.groupby(["Year", "Week"]).size().reset_index()[["Year", "Week"]]

total_weeks = len(all_weeks)

vehicle_weeks = weekly.groupby("Vehicle_ID")[["Year", "Week"]].nunique()

vehicle_weeks["Total_Weeks"] = vehicle_weeks["Week"]  # rename

habitual_offenders = vehicle_weeks[vehicle_weeks["Total_Weeks"] == total_weeks]

print("\nVehicles violating at least once EVERY week:")

print(habitual_offenders.index.tolist())
