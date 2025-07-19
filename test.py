import pandas as pd

# Load files
df1 = pd.read_excel(r"C:\Users\ansu2\Downloads\Registry\schools not taken attendance\Teachers Not taken attendance for entire April.xlsx")
df2 = pd.read_excel(r"C:\Users\ansu2\Downloads\Registry\schools not taken attendance\Teachers Not taken attendance for entire May.xlsx")
df3 = pd.read_excel(r"C:\Users\ansu2\Downloads\Registry\schools not taken attendance\Teachers Not taken attendance for entire June.xlsx")

# Get sets of teacher codes from each month
codes1 = set(df1["Teacher Code"])
codes2 = set(df2["Teacher Code"])
codes3 = set(df3["Teacher Code"])

# Find teacher codes common to all 3 months
common_codes = codes1 & codes2 & codes3

# Combine all data to pull full teacher details
combined_df = pd.concat([df1, df2, df3])

# Filter only those who are common in all 3
final_df = combined_df[combined_df["Teacher Code"].isin(common_codes)]

# Drop duplicates, keep just one row per teacher
final_df = final_df.drop_duplicates(subset=["Teacher Code"])

# Save to Excel
final_df.to_excel(r"C:\Users\ansu2\Downloads\Registry\schools not taken attendance\teachers_absent_all_3_months.xlsx", index=False)

print("✅ Final Excel generated: 'teachers_absent_all_3_months.xlsx'")
