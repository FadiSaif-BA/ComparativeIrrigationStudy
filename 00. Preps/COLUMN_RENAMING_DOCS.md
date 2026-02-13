# Irrigation Dataset - Column Renaming Documentation

## Overview
This document describes the column renaming scheme applied to `Irrigation_DS.xlsx` to create concise yet elaborative column names.

## Naming Convention
- **Format**: `Section_Subsection_Description`
- **Style**: PascalCase with underscores
- **Language**: English (for better code compatibility)
- **Principle**: Concise yet sufficiently descriptive

---

## Column Mapping by Section

### 📋 Survey Metadata (9 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| start | `Survey_Start_Time` | Survey start timestamp |
| end | `Survey_End_Time` | Survey end timestamp |
| اسم الماسح: | `Surveyor_Name` | Name of surveyor |
| تاريخ المسح | `Survey_Date` | Date of survey |
| المحافظة | `Governorate` | Governorate name |
| المحافظة: لحج | `Governorate_Lahj` | Specific: Lahj governorate |
| القرية | `Village_Name` | Village name |
| اسم المستفيد | `Beneficiary_Name` | Name of beneficiary |
| اسم المستجيب | `Respondent_Name` | Name of respondent |

### 🌾 Farm Information (2 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| Type of Irrigation system | `Irrigation_System_Type` | Type of irrigation system used |
| Type of crop growing | `Crop_Type` | Type of crop being grown |

---

### 🏗️ SECTION 1: Land Preparation (11 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| اولا: اعداد الارض | `Land_Prep_Section_Header` | Section header |
| total cost...plow...one acre | `Land_Prep_Plowing_Cost_Per_Acre` | Cost to plow 1 acre |
| total cost...settle...one acre | `Land_Prep_Settlement_Cost_Per_Acre` | Cost to settle 1 acre |
| total cost...divide...one acre | `Land_Prep_Division_Cost_Per_Acre` | Cost to divide 1 acre |
| total cost...terrace...one acre | `Land_Prep_Terracing_Cost_Per_Acre` | Cost to terrace 1 acre |
| total_cost | `Land_Prep_Total_Cost` | Total land prep material cost |
| How many workers...terracing | `Land_Prep_Workers_Count` | Number of workers needed |
| wage...worker per day per acre | `Land_Prep_Worker_Wage_Per_Day` | Daily wage per worker |
| How many days...work...acre | `Land_Prep_Working_Days` | Number of working days |
| total cost of worker...land | `Land_Prep_Labor_Total_Cost` | Total labor cost |
| Total cost of Land prepare | `Land_Prep_Grand_Total_Cost` | Grand total (materials + labor) |

---

### 🌱 SECTION 2: Nursery Preparation (2 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| ثانيا: اعداد المشتل | `Nursery_Prep_Section_Header` | Section header |
| total cost of seeding preparing | `Nursery_Prep_Total_Cost` | Total nursery/seeding prep cost |

---

### 🚜 SECTION 3: Permanent Land Cultivation (5 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| ثالثا: زراعة الارض المستديمة | `Cultivation_Section_Header` | Section header |
| How many labors...cultivate | `Cultivation_Laborers_Count` | Number of laborers for cultivation |
| cost of seeds...Quantity | `Cultivation_Seeds_Quantity` | Quantity of seeds/seedlings |
| wage of a worker per day | `Cultivation_Worker_Wage_Per_Day` | Daily wage per worker |
| cost of worker...sustainable land | `Cultivation_Labor_Total_Cost` | Total cultivation labor cost |

---

### 🧪 SECTION 4: Fertilization (4 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| Fertilization | `Fertilization_Section_Header` | Section header |
| fertilizer...Quantity in kg | `Fertilizer_Quantity_Kg` | Fertilizer quantity in kg |
| fertilizer...Cost (YER) | `Fertilizer_Cost_YER` | Fertilizer cost in YER |
| Total cost of fertilizer | `Fertilizer_Total_Cost` | Total fertilizer cost |

---

### 📦 SECTION 5: Production & Harvest (5 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| خامسا: Quantity of production | `Production_Section_Header` | Section header |
| Quantity of production...baskets/kg | `Production_Quantity_Baskets_Kg` | Production quantity |
| How many times...harvest...month | `Production_Harvest_Frequency_Per_Month` | Harvest frequency per month |
| الكلفة العامة لكمية المحصول | `Production_Total_Harvest_Cost` | Total harvest cost |
| cost of production and harvest | `Production_Harvest_Labor_Cost` | Harvest labor cost |

---

### 💰 SECTION 6: Production Cost (2 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| سادسا: Cost of production | `Production_Cost_Section_Header` | Section header |
| final production cost...YER | `Production_Final_Harvest_Cost_YER` | Final production cost in YER |

---

### 🐛 SECTION 7: Pest Control (12 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| سابعا:Pest Control | `Pest_Control_Section_Header` | Section header |
| ماهو نوع المكافحة | `Pest_Control_Type` | Type of pest control |
| مكافحة حيوية | `Pest_Control_Biological` | Biological control (natural enemies) |
| مكافحة ميكانيكية | `Pest_Control_Mechanical` | Mechanical control (traps, manual) |
| مكافحة كيمياوية | `Pest_Control_Chemical` | Chemical control (pesticides) |
| اخرى | `Pest_Control_Other` | Other (crop rotation, land service) |
| cost of...chemical...materials | `Pest_Control_Chemical_Materials_Cost` | Chemical materials cost |
| How many workers needed | `Pest_Control_Workers_Count` | Number of workers |
| wage...worker per day | `Pest_Control_Worker_Wage_Per_Day` | Daily wage per worker |
| no. of working day | `Pest_Control_Working_Days` | Number of working days |
| worker cost of pest control | `Pest_Control_Labor_Total_Cost` | Total labor cost |
| Total cost of Pest control | `Pest_Control_Grand_Total_Cost` | Grand total pest control cost |

---

### 💧 SECTION 8: Water Consumption (16 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| ثامنا: Amount of water consumed | `Water_Consumption_Section_Header` | Section header |
| Record the meters reading | `Water_Meter_Reading` | Water meter reading |
| hours...pumped...irrigation time | `Water_Pumping_Hours_Per_Irrigation` | Pumping hours per irrigation |
| times...irrigated...month | `Water_Irrigation_Frequency_Per_Month` | Irrigation frequency per month |
| Hr*time per month/6*20 | `Water_Calculated_Hours_Per_Month` | Calculated hours per month |
| cost of desile | `Water_Diesel_Cost` | Diesel cost |
| worker needed...irrigate | `Water_Workers_Count` | Number of workers |
| wage of worker per day | `Water_Worker_Wage_Per_Day` | Daily wage per worker |
| days per month | `Water_Working_Days_Per_Month` | Working days per month |
| total cost of worker | `Water_Labor_Total_Cost` | Total labor cost |
| Total cost...water and diesel | `Water_Grand_Total_Cost` | Grand total (water + diesel) |
| (spacer) | `Water_Additional_Info_Spacer` | Empty spacer column |
| pumping mechanism | `Water_Pumping_Mechanism_Type` | Type of pumping mechanism |
| hours...operate engine...acre | `Water_Engine_Hours_Per_Acre_Per_Day` | Engine hours per acre per day |
| diesel spent...acre...month | `Water_Diesel_Quantity_Last_Month` | Diesel quantity last month |
| cost of diesel...last month | `Water_Diesel_Cost_Last_Month` | Diesel cost last month |

---

### 📝 Other (2 columns)
| Old Name | New Name | Description |
|----------|----------|-------------|
| ملاحظات الماسح | `Surveyor_Notes` | Surveyor's notes/observations |
| _index | `Record_Index` | Record index number |

---

## Summary Statistics
- **Total Columns**: 68
- **Survey Metadata**: 9 columns
- **Farm Information**: 2 columns
- **Land Preparation**: 11 columns
- **Nursery Preparation**: 2 columns
- **Cultivation**: 5 columns
- **Fertilization**: 4 columns
- **Production & Harvest**: 5 columns
- **Production Cost**: 2 columns
- **Pest Control**: 12 columns
- **Water Consumption**: 16 columns
- **Other**: 2 columns

## Usage
Run the `rename_columns.py` script to apply these changes:
```python
python rename_columns.py
```

The script will:
1. Create a timestamped backup of the original file
2. Apply the column renaming
3. Save the updated file with new column names
