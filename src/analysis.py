from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt

class SolarAnalyzer:
    """Analyze and compare solar energy datasets for multiple countries."""

    def __init__(self, data_files: Dict[str, str]):
        """Takes a dictionary of country names and their file paths."""
        self.data_files = data_files
        self.datasets: Dict[str, pd.DataFrame] = {}

    def load_data(self) -> None:
        """Load all datasets into memory."""
        for country, path in self.data_files.items():
            self.datasets[country] = pd.read_csv(path)

    def summarize(self) -> pd.DataFrame:
        """Return a DataFrame summarizing mean GHI, DNI, DHI per country."""
        summary = pd.DataFrame({
            c: [
                self.datasets[c]["GHI"].mean(),
                self.datasets[c]["DNI"].mean(),
                self.datasets[c]["DHI"].mean(),
            ]
            for c in self.datasets
        }).T
        summary.columns = ["Mean_GHI", "Mean_DNI", "Mean_DHI"]
        return summary

    def plot_comparison(self) -> None:
        """Plot boxplots comparing solar radiation metrics across countries."""
        data = [self.datasets[c]["GHI"] for c in self.datasets]
        plt.boxplot(data, labels=self.datasets.keys())
        plt.title("Global Horizontal Irradiance (GHI) by Country")
        plt.ylabel("GHI (W/m²)")
        plt.show()
