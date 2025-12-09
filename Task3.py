# Task 3
# To get more insight into the factors behind product quality, you want to filter the data to see an average product quality score for a specified set of results.

# Identify the average product_quality_score for batches with a raw_material_supplier of 2 and a pigment_quantity greater than 35 kg.

# Write a query to return the average avg_product_quality_score for these filtered batches. Use the original production data table, not the output of Task 2.

# You should start with the data in the file 'production_data.csv'.
# Your output should be a DataFrame named pigment_data.
# It should consist of a 1-row DataFrame with 3 columns: raw_material_supplier, pigment_quantity, and avg_product_quality_score.
# Your answers should be rounded to 2 decimal places where appropriate.

                   # CODE FOR THE TASK 3 BELOW
                   


import pandas as pd
import numpy as np

# Load original data
df = pd.read_csv("production_data.csv")

# Convert needed columns
df['pigment_quantity'] = pd.to_numeric(df['pigment_quantity'], errors='coerce')
df['product_quality_score'] = pd.to_numeric(df['product_quality_score'], errors='coerce')

# Filter conditions
filtered = df[
    (df['raw_material_supplier'] == 2) &
    (df['pigment_quantity'] > 35)
]

# Compute means
avg_quality = round(filtered['product_quality_score'].mean(), 2)
avg_pigment = round(filtered['pigment_quantity'].mean(), 2)

# Build output DataFrame
pigment_data = pd.DataFrame({
    'raw_material_supplier': [2],
    'pigment_quantity': [avg_pigment],
    'avg_product_quality_score': [avg_quality]
})

pigment_data
