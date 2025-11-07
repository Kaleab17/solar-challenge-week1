"""
utils.py
This module contains helper functions for cleaning and analyzing solar data.
Author: Kaleab Million
"""

import pandas as pd
import numpy as np

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in numeric columns with their median.

    Args:
        df (pd.DataFrame): The input dataset.

    Returns:
        pd.DataFrame: Dataset with missing values handled.
    """
    df.fillna(df.median(), inplace=True)
    return df


def remove_outliers(df: pd.DataFrame, columns: list, threshold: float = 3.0) -> pd.DataFrame:
    """
    Remove outliers using the Z-score method.

    Args:
        df (pd.DataFrame): Input dataset.
        columns (list): Numeric columns to check for outliers.
        threshold (float): Z-score threshold for removal (default=3.0).

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    from scipy import stats
    z = np.abs(stats.zscore(df[columns]))
    df = df[(z < threshold).all(axis=1)]
    return df
