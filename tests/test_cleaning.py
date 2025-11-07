"""
Simple test for DataCleaner and DataValidator
"""

import pandas as pd
from src.utils import DataCleaner, DataValidator

def test_cleaning_pipeline():
    data = {
        "GHI": [100, 200, None, 250],
        "DNI": [50, 80, None, 120],
        "Tamb": [25, None, 27, 29],
    }

    df = pd.DataFrame(data)
    validator = DataValidator(df)
    validator.check_missing()

    cleaner = DataCleaner(df)
    df_cleaned = cleaner.handle_missing().remove_outliers(["GHI", "DNI", "Tamb"]).df

    validator = DataValidator(df_cleaned)
    validator.check_ranges()
