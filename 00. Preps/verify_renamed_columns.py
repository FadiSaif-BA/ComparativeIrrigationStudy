import pandas as pd
import sys

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Load the renamed Excel file
df = pd.read_excel('Irrigation_DS.xlsx')

print("=" * 80)
print("VERIFICATION: Renamed Column Structure")
print("=" * 80)
print(f"\nTotal columns: {len(df.columns)}")
print(f"Total rows: {len(df)}\n")

# Group columns by section
sections = {
    'Survey Metadata': [col for col in df.columns if col.startswith('Survey_') or col.startswith('Surveyor_') or col in ['Governorate', 'Governorate_Lahj', 'Village_Name', 'Beneficiary_Name', 'Respondent_Name']],
    'Farm Information': [col for col in df.columns if col.startswith('Irrigation_System') or col.startswith('Crop_')],
    'Land Preparation': [col for col in df.columns if col.startswith('Land_Prep_')],
    'Nursery Preparation': [col for col in df.columns if col.startswith('Nursery_')],
    'Cultivation': [col for col in df.columns if col.startswith('Cultivation_')],
    'Fertilization': [col for col in df.columns if col.startswith('Fertiliz')],
    'Production & Harvest': [col for col in df.columns if col.startswith('Production_')],
    'Pest Control': [col for col in df.columns if col.startswith('Pest_')],
    'Water Consumption': [col for col in df.columns if col.startswith('Water_')],
    'Other': [col for col in df.columns if col in ['Surveyor_Notes', 'Record_Index']]
}

# Display sections
for section_name, columns in sections.items():
    if columns:
        print(f"\n{section_name} ({len(columns)} columns):")
        print("-" * 80)
        for col in columns:
            print(f"  • {col}")

# Check for any unmapped columns
all_sectioned = []
for cols in sections.values():
    all_sectioned.extend(cols)

unmapped = [col for col in df.columns if col not in all_sectioned]
if unmapped:
    print(f"\nUnmapped columns ({len(unmapped)}):")
    print("-" * 80)
    for col in unmapped:
        print(f"  • {col}")

# Sample data display
print("\n" + "=" * 80)
print("Sample Data (First 3 rows - Key columns):")
print("=" * 80)
key_columns = ['Surveyor_Name', 'Survey_Date', 'Village_Name', 'Crop_Type', 'Irrigation_System_Type']
existing_key_columns = [col for col in key_columns if col in df.columns]
if existing_key_columns:
    print(df[existing_key_columns].head(3).to_string(index=False))

print("\n" + "=" * 80)
print("✓ VERIFICATION COMPLETE!")
print("=" * 80)
