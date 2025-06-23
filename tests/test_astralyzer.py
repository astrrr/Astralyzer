import os
import tempfile
import pandas as pd
import numpy as np
from astralyzer import Astralyzer
import pytest


def create_temp_csv():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2024-01-01', '2024-01-02'],
        'Time': ['09:00:00', '10:00:00', '09:00:00', '10:00:00'],
        'Open': [100, 102, 110, 111],
        'High': [105, 106, 112, 113],
        'Low': [95, 98, 108, 109],
        'Close': [102, 103, 111, 112],
        'Volume': [500, 450, 500, 450],
    }
    df = pd.DataFrame(data)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(tmp.name, index=False)
    tmp.close()
    return tmp.name, df


def test_calculate_stats_close():
    path, df = create_temp_csv()
    try:
        analyzer = Astralyzer(path, "Test")
        mean, std, *_ = analyzer.calculate_stats("Close")
        assert mean == pytest.approx(np.mean(df["Close"]))
        assert std == pytest.approx(np.std(df["Close"]))
    finally:
        os.unlink(path)


def test_separate_df_by_year():
    path, df = create_temp_csv()
    try:
        analyzer = Astralyzer(path, "Test")
        year_dict = analyzer.separate_df_by_year()
        expected_years = set(pd.to_datetime(df["Date"]).dt.year.unique())
        assert set(year_dict.keys()) == expected_years
    finally:
        os.unlink(path)
