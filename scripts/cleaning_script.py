"""
cleaning_script.py
Simple demonstration of data cleaning using utility functions.
Author: Kaleab Million
"""

import pandas as pd
from src.utils import handle_missing_values, remove_outliers

# Create sample data
data = {
    "GHI": [100, 200, None, 250, 3000],
    "DNI": [50, None, 75, 100, 5000],
    "Tamb": [25, 27, None, 29, 45]
}

df = pd.DataFrame(data)

print("Before cleaning:")
print(df)

# Handle missing values and remove outliers
df = handle_missing_values(df)
df = remove_outliers(df, ["GHI", "DNI", "Tamb"])

print("\nAfter cleaning:")
print(df)
