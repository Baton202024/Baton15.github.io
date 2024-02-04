import pandas as pd

# Using raw string literals
excel_file = r"C:\Users\marlo\Downloads\SampleXLSFile_212kb.xlsx"
df = pd.read_excel(excel_file)

# Add a new column "Profit" which is the difference between Revenue and Cost
print(df.head())