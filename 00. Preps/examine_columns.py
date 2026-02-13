import pandas as pd

# Load the Excel file
df = pd.read_excel('Irrigation_DS.xlsx')

# Display current columns
print("=" * 60)
print("CURRENT COLUMN NAMES:")
print("=" * 60)
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print(f"\nTotal columns: {len(df.columns)}")
print(f"Total rows: {len(df)}")

# Display first few rows to understand data
print("\n" + "=" * 60)
print("FIRST 3 ROWS OF DATA:")
print("=" * 60)
print(df.head(3))

# Show data types
print("\n" + "=" * 60)
print("COLUMN DATA TYPES:")
print("=" * 60)
print(df.dtypes)
