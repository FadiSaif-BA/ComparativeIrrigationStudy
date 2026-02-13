"""
Create Tableau-Ready Dataset for Irrigation Study
This script combines the clean irrigation data with all derived variables
created during analysis for easy use in Tableau dashboards.
"""

import pandas as pd
import numpy as np

print("="*80)
print("CREATING TABLEAU-READY IRRIGATION DATASET")
print("="*80)

# Load the cleaned dataset
print("\n1. Loading cleaned data...")
df = pd.read_excel('Irrigation_DS_Clean.xlsx')
print(f"   ✓ Loaded {len(df)} rows with {len(df.columns)} columns")

# ============================================================================
# DERIVED VARIABLES - As created in Cost-Benefit Analysis
# ============================================================================
print("\n2. Creating derived cost variables...")

# Define cost columns for aggregation
cost_columns = [
    'land_prep_grand_total_cost',
    'nursery_prep_total_cost',
    'cultivation_labor_total_cost',
    'fertilizer_total_cost',
    'production_final_harvest_cost_yer',
    'pest_control_grand_total_cost',
    'water_grand_total_cost'
]

# Calculate total cost per record
df['total_cost'] = df[cost_columns].sum(axis=1)
print(f"   ✓ Created 'total_cost' variable")

# Define benefit metric (production quantity)
df['production_kg'] = df['production_quantity_baskets_kg']
print(f"   ✓ Created 'production_kg' variable")

# Calculate cost-benefit metrics
# Cost per kg (avoiding division by zero)
df['cost_per_kg'] = np.where(
    df['production_kg'] > 0,
    df['total_cost'] / df['production_kg'],
    np.nan
)
print(f"   ✓ Created 'cost_per_kg' variable")

# Production efficiency (kg per 1000 YER)
df['production_efficiency'] = np.where(
    df['total_cost'] > 0,
    df['production_kg'] / df['total_cost'] * 1000,
    np.nan
)
print(f"   ✓ Created 'production_efficiency' variable")

# ============================================================================
# ADDITIONAL USEFUL DERIVED VARIABLES
# ============================================================================
print("\n3. Creating additional derived variables...")

# Cost category percentages
for col in cost_columns:
    pct_col_name = f'{col}_pct'
    df[pct_col_name] = np.where(
        df['total_cost'] > 0,
        (df[col] / df['total_cost']) * 100,
        np.nan
    )
    print(f"   ✓ Created '{pct_col_name}' variable")

# Irrigation system indicator flag (for easier filtering in Tableau)
df['is_drip_irrigation'] = (df['irrigation_system_type'] == 'Drip').astype(int)
df['is_traditional_irrigation'] = (df['irrigation_system_type'] == 'Traditional').astype(int)
print(f"   ✓ Created irrigation system indicator variables")

# Date features (if needed for time-series analysis)
if 'survey_date' in df.columns:
    df['survey_year'] = pd.to_datetime(df['survey_date']).dt.year
    df['survey_month'] = pd.to_datetime(df['survey_date']).dt.month
    df['survey_month_name'] = pd.to_datetime(df['survey_date']).dt.month_name()
    print(f"   ✓ Created date-related variables")

# ============================================================================
# REMOVE UNNECESSARY COLUMNS
# ============================================================================
print("\n4. Cleaning up dataset...")

# Remove section header columns (they're just placeholders)
section_headers = [
    'land_prep_section_header',
    'nursery_prep_section_header',
    'cultivation_section_header',
    'fertilization_section_header',
    'production_section_header',
    'production_cost_section_header',
    'pest_control_section_header',
    'water_consumption_section_header',
    'water_additional_info_spacer'
]

columns_to_drop = [col for col in section_headers if col in df.columns]
if columns_to_drop:
    df = df.drop(columns=columns_to_drop)
    print(f"   ✓ Removed {len(columns_to_drop)} unnecessary header columns")

# ============================================================================
# EXPORT TO MULTIPLE FORMATS
# ============================================================================
print("\n5. Exporting dataset...")

# Export to Excel (primary format for Tableau)
excel_file = 'Irrigation_Analysis_Tableau_Ready.xlsx'
df.to_excel(excel_file, index=False, sheet_name='Irrigation Data')
print(f"   ✓ Exported to Excel: {excel_file}")

# Export to CSV (alternative format)
csv_file = 'Irrigation_Analysis_Tableau_Ready.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"   ✓ Exported to CSV: {csv_file}")

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Total Records: {len(df)}")
print(f"Total Variables: {len(df.columns)}")
print(f"\nOriginal Variables: {len(df.columns) - len(cost_columns) - 11}")  # Approximation
print(f"Derived Variables: ~{len(cost_columns) + 11}")
print(f"\nIrrigation System Breakdown:")
print(df['irrigation_system_type'].value_counts().to_string())
print(f"\nCrop Type Breakdown:")
print(df['crop_type'].value_counts().to_string())
print(f"\nMissing Values Summary (Top 5):")
missing_summary = df.isnull().sum().sort_values(ascending=False).head()
if missing_summary.sum() > 0:
    print(missing_summary.to_string())
else:
    print("   No missing values!")

print("\n" + "="*80)
print("✓ TABLEAU-READY DATASET CREATED SUCCESSFULLY!")
print("="*80)
print(f"\nYou can now import '{excel_file}' into Tableau")
print("All original variables plus derived cost-benefit metrics are included.")
