# Task 2
# You want to understand how the supplier type and quantity of materials affect the final product attributes.

# Calculate the average product_quality_score and pigment_quantity grouped by raw_material_supplier.

# You should start with the data in the file 'production_data.csv'.
# Your output should be a DataFrame named aggregated_data.
# It should include the three columns: raw_material_supplier, avg_product_quality_score, and avg_pigment_quantity.
# Your answers should be rounded to 2 decimal places.

import pandas as pd

# Load the data
df = pd.read_csv("production_data.csv")

#  Clean minimal columns needed for grouping

# Raw material supplier mapping
supplier_map = {1: 'national_supplier', 2: 'international_supplier'}
df['raw_material_supplier'] = df['raw_material_supplier'].map(supplier_map)
df['raw_material_supplier'] = df['raw_material_supplier'].fillna('national_supplier')

# Ensure numeric columns
df['product_quality_score'] = pd.to_numeric(df['product_quality_score'], errors='coerce')
df['pigment_quantity'] = pd.to_numeric(df['pigment_quantity'], errors='coerce')

# Group and calculate averages
aggregated_data = df.groupby('raw_material_supplier').agg(
    avg_product_quality_score = ('product_quality_score', lambda x: round(x.mean(), 2)),
    avg_pigment_quantity = ('pigment_quantity', lambda x: round(x.mean(), 2))
).reset_index()

aggregated_data