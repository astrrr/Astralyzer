# Astralyzer

**Astralyzer** is a Python-based tool designed for analyzing financial data from CSV files that exported from MetaTrader. It provides various functionalities for data processing, statistical analysis, and visualization of metrics such as volatility and closing prices. 

## Features
- Load and preprocess financial data
- Calculate statistical values with standard deviation bounds
- Separate data by year for annual analysis
- Visualize volatility and closing prices across multiple years

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## Installation

You can install the package via pip:
```
pip install git+https://github.com/astrrr/Astralyzer.git
```


## Usage

### 1. Initialize Astralyzer

Instantiate the `Astralyzer` class with the path to your CSV file and the product name.

```python
from astralyzer import Astralyzer

analyzer = Astralyzer(filepath="path/to/your/data.csv", product_name="Sample Product")
```

### 2. Calculate Statistics

Calculate the mean and standard deviations for a specific column, such as `'Volatility'` or `'Close'`. This method returns the mean, standard deviation, and bounds for ±1, ±2, and ±3 standard deviations.

```python
mean, std, *std_bounds = analyzer.calculate_stats("Volatility")
print("Mean:", mean)
print("Standard Deviations Bounds:", std_bounds)
```

### 3. Separate Data by Year

Separate data into yearly segments for individual analysis.

```python
yearly_data = analyzer.separate_df_by_year()
print(yearly_data[2023].head())  # Data for the year 2023
```

### 4. Visualize Data

#### Volatility Histogram

Generate a histogram of volatility with mean and standard deviation lines:

```python
analyzer.visualize_volatility(width=10, height=6)
```

#### Close Price Histogram

Generate a histogram of closing prices with mean and standard deviation lines:

```python
analyzer.visualize_close(width=10, height=6)
```

#### Yearly Close Price Histogram

Visualize close prices for each year in individual charts or combined in one chart:

```python
analyzer.visualize_close_each_year(width=12, height=6, bins=30, one_chart_per_year=True)
```

#### Yearly Volatility Histogram

Visualize volatility for each year in individual charts or combined in one chart:

```python
analyzer.visualize_volatility_each_year(width=12, height=6, bins=30, one_chart_per_year=True)
```

## Example Data Format

Ensure your CSV data is structured with columns:
- `Date` (e.g., `YYYY-MM-DD`)
- `Time` (e.g., `HH:MM:SS`)
- `Open`, `High`, `Low`, `Close`, `Volume`

Example:
```csv
Date,Time,Open,High,Low,Close,Volume
2023-01-01,09:00:00,100,105,95,102,500
2023-01-01,10:00:00,102,106,98,104,450
```

## Exporting Data from MT4/MT5
In MT4 or MT5:

1. Open the `History Center` (F2).
2. Select the asset (e.g., EURUSD) and timeframe you want to export.
3. Click `Export` to save the data as a `.csv` file.

## License

This project is licensed under the MIT License.

--- 
