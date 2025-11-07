import pandas as pd

class DataCleaner:
    """A class to clean solar energy data."""

    def __init__(self, df: pd.DataFrame):
        """Initialize with a dataset."""
        self.df = df

    def handle_missing(self) -> 'DataCleaner':
        """Fill missing values with the median for each column."""
        self.df = self.df.fillna(self.df.median(numeric_only=True))
        return self

    def remove_outliers(self, columns: list[str]) -> 'DataCleaner':
        """Remove outliers from given columns using the 5th and 95th percentiles."""
        for col in columns:
            if col in self.df.columns:
                q_low = self.df[col].quantile(0.05)
                q_high = self.df[col].quantile(0.95)
                self.df = self.df[(self.df[col] >= q_low) & (self.df[col] <= q_high)]
        return self

    def save_cleaned(self, filename: str) -> None:
        """Save the cleaned dataset to a CSV file."""
        self.df.to_csv(filename, index=False)


class DataValidator:
    """A helper class to validate the dataset before and after cleaning."""

    def __init__(self, df: pd.DataFrame):
        """Initialize with the dataset."""
        self.df = df

    def check_missing(self) -> int:
        """Return the total number of missing values."""
        missing = self.df.isna().sum().sum()
        print(f"Missing values: {missing}")
        return missing

    def check_ranges(self) -> None:
        """Check if key columns fall within expected value ranges."""
        if "GHI" in self.df.columns:
            print(f"GHI range: {self.df['GHI'].min()} - {self.df['GHI'].max()}")
        if "DNI" in self.df.columns:
            print(f"DNI range: {self.df['DNI'].min()} - {self.df['DNI'].max()}")
