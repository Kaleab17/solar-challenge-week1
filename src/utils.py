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
