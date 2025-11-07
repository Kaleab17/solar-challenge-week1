"""
pipeline.py
Pipeline orchestrator that runs cleaning for all country datasets.
Author: Kaleab Million
"""

import pandas as pd
from src.utils import DataCleaner, DataValidator

# Dictionary of all countries and their data files
countries = {
    "Benin": "data/benin.csv",
    "SierraLeone": "data/sierra_leone.csv",
    "Togo": "data/togo.csv"
}

# Loop through each country and process the dataset
for country, path in countries.items():
    print(f"\nProcessing {country} dataset...")

    # Load raw data
    df = pd.read_csv(path)

    # Validate the dataset before cleaning
    validator = DataValidator(df)
    validator.check_missing()

    # Clean data: handle missing values and remove outliers
    cleaner = DataCleaner(df)
    cleaner.handle_missing().remove_outliers(["GHI", "DNI", "DHI", "Tamb"])

    # Save the cleaned version
    cleaner.save_cleaned(f"data/{country.lower()}_clean.csv")

    # Validate again after cleaning
    validator = DataValidator(cleaner.df)
    validator.check_ranges()

print("\nAll countries processed successfully!")
