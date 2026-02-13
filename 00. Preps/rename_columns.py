import pandas as pd
from datetime import datetime
import sys

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Load the Excel file
df = pd.read_excel('Irrigation_DS.xlsx')

print("=" * 80)
print("BEFORE RENAMING:")
print("=" * 80)
print(f"Total columns: {len(df.columns)}")
print(f"Total rows: {len(df)}\n")

# Create a comprehensive column mapping - Concise yet Elaborative
column_mapping = {
    'start': 'Survey_Start_Time',
    'end': 'Survey_End_Time',
    'اسم الماسح:': 'Surveyor_Name',
    'تاريخ المسح': 'Survey_Date',
    'المحافظة': 'Governorate',
    'المحافظة: لحج': 'Governorate_Lahj',
    'القرية': 'Village_Name',
    'اسم المستفيد': 'Beneficiary_Name',
    'اسم المستجيب': 'Respondent_Name',
    ' Type of Irrigation system': 'Irrigation_System_Type',
    'Type of crop growing': 'Crop_Type',
    
    # SECTION 1: Land Preparation
    ' اولا: اعداد الارض:(ساعات*اجرة) ': 'Land_Prep_Section_Header',
    'total cost take to plow the area of \u200b\u200b one acre connected to the meter?': 'Land_Prep_Plowing_Cost_Per_Acre',
    'total cost take to settle the area of one acre': 'Land_Prep_Settlement_Cost_Per_Acre',
    'total cost take to divide the area of \u200b\u200bone acre connected to the meter?': 'Land_Prep_Division_Cost_Per_Acre',
    'total cost take to terrace the area of one acre connected to the meter?': 'Land_Prep_Terracing_Cost_Per_Acre',
    'total_cost': 'Land_Prep_Total_Cost',
    'How many workers were needed to raise the terracing and canals ': 'Land_Prep_Workers_Count',
    'How much was the wage of a worker per day per acre connected to the meter': 'Land_Prep_Worker_Wage_Per_Day',
    'How many days were needed to work on this acre?': 'Land_Prep_Working_Days',
    'total cost of worker to prepare the land': 'Land_Prep_Labor_Total_Cost',
    'Total cost of Land prepare': 'Land_Prep_Grand_Total_Cost',
    
    # SECTION 2: Nursery/Seedling Preparation
    '  ثانيا: اعداد المشتل  ': 'Nursery_Prep_Section_Header',
    'total cost of seeding preparing': 'Nursery_Prep_Total_Cost',
    
    # SECTION 3: Permanent Land Cultivation
    'ثالثا: زراعة الارض المستديمة: *يتم اجراء هذا المسح في الشهر الاول و الثاني': 'Cultivation_Section_Header',
    'How many labors were needed to cultivate one acre of …………………… (tomatoes / onions / green jalapino / Leafy plants / okra) ': 'Cultivation_Laborers_Count',
    'How much was the cost of seeds / seedlings planted per acre: The amount of seeds (Quantity)': 'Cultivation_Seeds_Quantity',
    'How much was the wage of a worker per day?': 'Cultivation_Worker_Wage_Per_Day',
    'The cost of the worker in cultivating sustainable land': 'Cultivation_Labor_Total_Cost',
    
    # SECTION 4: Fertilization
    'Fertilization': 'Fertilization_Section_Header',
    'How much was the cost of the fertilizer you used in the one acer connected to the meter? (Quantity in kg)': 'Fertilizer_Quantity_Kg',
    'How much was the cost of the fertilizer you used in the one acer connected to the meter? (Cost (YER))': 'Fertilizer_Cost_YER',
    'Total cost of fertilizer ': 'Fertilizer_Total_Cost',
    
    # SECTION 5: Production and Harvest
    'خامسا: Quantity of production and harvest': 'Production_Section_Header',
    'Quantity of production in the last cultivation season (number of baskets / kg)': 'Production_Quantity_Baskets_Kg',
    'How many times did you harvest the planted items in the last month? ': 'Production_Harvest_Frequency_Per_Month',
    'الكلفة العامة لكمية المحصول': 'Production_Total_Harvest_Cost',
    'cost of  production and harvest': 'Production_Harvest_Labor_Cost',
    
    # SECTION 6: Production Cost
    'سادسا: Cost of production: ': 'Production_Cost_Section_Header',
    'How much was the final production cost needed for harvesting in YER': 'Production_Final_Harvest_Cost_YER',
    
    # SECTION 7: Pest Control
    'سابعا:Pest Control': 'Pest_Control_Section_Header',
    ' ماهو نوع المكافحة المستخدمة': 'Pest_Control_Type',
    ' ماهو نوع المكافحة المستخدمة/مكافحة حيوية (استخدام الاعداء الطبيعية منها: المفترسات و المتطفلات مثل النمل)': 'Pest_Control_Biological',
    ' ماهو نوع المكافحة المستخدمة/مكافحة ميكانيكية (جمع الحشرات الكبيرة باليد وا ستخدام التدخين واستخدام المصائد الضوئية و الفورمونية)': 'Pest_Control_Mechanical',
    ' ماهو نوع المكافحة المستخدمة/مكافحة كيمياوية (باستخدام المبيدات)': 'Pest_Control_Chemical',
    ' ماهو نوع المكافحة المستخدمة/اخرى(باستخدام الدورة الزراعية, خدمة الارض مثل تقليب الارض/ ازالة الحشائش / الري والتسميد/ زراعة الاصناف المقاومة للافات)': 'Pest_Control_Other',
    'If the answer (chemical control) how much was the cost of its materials:': 'Pest_Control_Chemical_Materials_Cost',
    'How many workers were needed?': 'Pest_Control_Workers_Count',
    'How much was the wage of the worker per day?': 'Pest_Control_Worker_Wage_Per_Day',
    'no. of working day': 'Pest_Control_Working_Days',
    'worker cost of pest control': 'Pest_Control_Labor_Total_Cost',
    'Total cost of Pest control': 'Pest_Control_Grand_Total_Cost',
    
    # SECTION 8: Water Consumption
    ' ثامنا: Amount of water consumed': 'Water_Consumption_Section_Header',
    'Record the meters reading': 'Water_Meter_Reading',
    'How many hours the water pumped in one irrigation time?': 'Water_Pumping_Hours_Per_Irrigation',
    'How many times the land was irrigated in the last month?': 'Water_Irrigation_Frequency_Per_Month',
    'Hr*time per month/6*20': 'Water_Calculated_Hours_Per_Month',
    'cost of desile': 'Water_Diesel_Cost',
    'no of worker needed to irrigate the land': 'Water_Workers_Count',
    'wage of worker per day': 'Water_Worker_Wage_Per_Day',
    'no of days per month': 'Water_Working_Days_Per_Month',
    'total cost of worker': 'Water_Labor_Total_Cost',
    'Total cost of water and diesel consumption': 'Water_Grand_Total_Cost',
    
    # Additional Water/Diesel Info
    '      ': 'Water_Additional_Info_Spacer',
    'What is the applied pumping mechanism': 'Water_Pumping_Mechanism_Type',
    'The number of hours were needed to operate the engine to irrigate the acre per day:': 'Water_Engine_Hours_Per_Acre_Per_Day',
    'What was the amount of diesel spent to irrigate the area of the acre in the last month?': 'Water_Diesel_Quantity_Last_Month',
    'How much was the cost of diesel spent in the last month?': 'Water_Diesel_Cost_Last_Month',
    
    # Other
    'ملاحظات الماسح': 'Surveyor_Notes',
    '_index': 'Record_Index'
}

# Apply the renaming
df_renamed = df.rename(columns=column_mapping)

# Display the mapping
print("COLUMN RENAMING MAPPING:")
print("=" * 80)
for i, (old, new) in enumerate(column_mapping.items(), 1):
    print(f"{i:2d}. {old[:50]:50s} -> {new}")

print("\n" + "=" * 80)
print("AFTER RENAMING:")
print("=" * 80)
print(f"Total columns: {len(df_renamed.columns)}")
print(f"Total rows: {len(df_renamed)}\n")

print("New column names:")
for i, col in enumerate(df_renamed.columns, 1):
    print(f"{i:2d}. {col}")

# Create backup of original file
backup_filename = f'Irrigation_DS_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
print(f"\n" + "=" * 80)
print(f"Creating backup: {backup_filename}")
df.to_excel(backup_filename, index=False)
print("Backup created successfully!")

# Save the renamed dataframe
output_filename = 'Irrigation_DS.xlsx'
print(f"\nSaving renamed columns to: {output_filename}")
df_renamed.to_excel(output_filename, index=False)
print("File saved successfully!")

print("\n" + "=" * 80)
print("RENAMING COMPLETE!")
print("=" * 80)
print(f"✓ Original file backed up as: {backup_filename}")
print(f"✓ Renamed file saved as: {output_filename}")
print(f"✓ {len(column_mapping)} columns renamed")
