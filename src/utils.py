class DataCleaner:
    """
    A reusable class for cleaning and processing solar datasets.
    """

    def __init__(self, df):
        self.df = df

    def handle_missing(self):
        """Fill missing numeric values with the median."""
        self.df.fillna(self.df.median(), inplace=True)
        return self

    def remove_outliers(self, columns, threshold=3.0):
        """Remove outliers based on Z-score."""
        from scipy import stats
        z = np.abs(stats.zscore(self.df[columns]))
        self.df = self.df[(z < threshold).all(axis=1)]
        return self

    def save_cleaned(self, output_path):
        """Save cleaned data to a CSV file."""
        self.df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
        return self

class DataValidator:
    """
    A small helper class to validate solar datasets before and after cleaning.
    """

    def __init__(self, df):
        self.df = df

    def check_missing(self):
        """Print number of missing values in each column."""
        print("Missing values by column:")
        print(self.df.isna().sum())
        return self

    def check_ranges(self):
        """Check for negative or extreme values in solar radiation columns."""
        bad_values = self.df[(self.df["GHI"] < 0) | (self.df["DNI"] < 0)]
        if not bad_values.empty:
            print(" Warning: Found invalid radiation readings.")
        else:
            print(" All radiation values are within valid range.")
        return self

