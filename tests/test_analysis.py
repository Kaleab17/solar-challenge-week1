"""
test_analysis.py
Simple unit test for SolarAnalyzer class.
"""

import pandas as pd
from src.analysis import SolarAnalyzer

def test_summarize():
    # Create sample CSVs for testing
    df1 = pd.DataFrame({"GHI": [100, 200], "DNI": [50, 100], "DHI": [20, 30]})
    df2 = pd.DataFrame({"GHI": [150, 250], "DNI": [60, 110], "DHI": [25, 35]})
    df1.to_csv("data/test_country1.csv", index=False)
    df2.to_csv("data/test_country2.csv", index=False)

    analyzer = SolarAnalyzer({
        "Country1": "data/test_country1.csv",
        "Country2": "data/test_country2.csv"
    })
    analyzer.load_data()
    summary = analyzer.summarize()
    assert not summary.empty, "Summary table should not be empty."
