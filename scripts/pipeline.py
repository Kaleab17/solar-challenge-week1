"""
pipeline.py
Pipeline orchestrator that runs cleaning for all country datasets.
"""

import pandas as pd
from src.utils import DataCleaner

countries = {
    "Benin": "data/benin.csv",
    "SierraLeone": "data/sierra_leone.csv",
    "Togo": "data/togo.csv"
}

for country, path in countries.items():
    print(f"\n Processing {country} dataset...")

    df = pd.read_csv(path)
    cleaner = DataCleaner(df)
    cleaner.handle_missing().remove_outliers(["GHI", "DNI", "DHI", "Tamb"])
    cleaner.save_cleaned(f"data/{country.lower()}_clean.csv")

print("\n All countries processed successfully!")
