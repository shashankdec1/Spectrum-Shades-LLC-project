# Task 1
# Before you can start any analysis, you need to confirm that the data is accurate and reflects what you expect to see.

# It is known that there are some issues with the production_data table, and the data team have provided the following data description.

# Write a query to ensure the data matches the description provided, including identifying and cleaning all invalid values. You must match all column names and description criteria.

# You should start with the data in the file "production_data.csv".
# Your output should be a DataFrame named clean_data.
# All column names and values should match the table below.

# Column Name	Criteria
# batch_id	Discrete. Identifier for each batch. Missing values are not possible.
# production_date	Date. Date when the batch was produced.
# raw_material_supplier	Categorical. Supplier of the raw materials. (1='national_supplier', 2='international_supplier').
# Missing values should be replaced with 'national_supplier'.
# pigment_type	Nominal. Type of pigment used. ['type_a', 'type_b', 'type_c'].
# Missing values should be replaced with 'other'.
# pigment_quantity	Continuous. Amount of pigment added (in kilograms) (Range: 1 - 100).
# Missing values should be replaced with median.
# mixing_time	Continuous. Duration of the mixing process (in minutes).
# Missing values should be replaced with mean, rounded to 2 decimal places.
# mixing_speed	Categorical. Speed of the mixing process represented as categories: 'Low', 'Medium', 'High'.
# Missing values should be replaced with 'Not Specified'.
# product_quality_score	Continuous. Overall quality score of the final product (rating on a scale of 1 to 10).
# Missing values should be replaced with mean, rounded to 2 decimal places.


                   # CODE FOR THE TASK 1 BELOW
                   
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("production_data.csv")

# CLEAN CATEGORICAL & TEXT DATA
# Normalize column names (string manipulation)
df.columns = df.columns.str.strip().str.lower()

# raw_material_supplier 
# Converting to proper categorical values by mapping 1/2 → text
supplier_map = {1: 'national_supplier', 2: 'international_supplier'}
df['raw_material_supplier'] = df['raw_material_supplier'].map(supplier_map)

# Replace missing/invalid supplier with national_supplier
df['raw_material_supplier'] = df['raw_material_supplier'].fillna('national_supplier')

# pigment_type
# Clean text: lowercase, strip spaces
df['pigment_type'] = df['pigment_type'].astype(str).str.strip().str.lower()

valid_pigments = ['type_a', 'type_b', 'type_c']

# Replace invalid & missing values to "other"
df['pigment_type'] = df['pigment_type'].where(df['pigment_type'].isin(valid_pigments), 'other')

#  mixing_speed
# Clean string values: capitalize first letter for consistency
df['mixing_speed'] = df['mixing_speed'].astype(str).str.strip().str.capitalize()

valid_speeds = ['Low', 'Medium', 'High']

# Replace invalid or missing values to "Not Specified"
df['mixing_speed'] = df['mixing_speed'].where(df['mixing_speed'].isin(valid_speeds), 'Not Specified')

# Output cleaned DataFrame for Task 1
clean_data = df.copy()
clean_data