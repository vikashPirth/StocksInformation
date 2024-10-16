
# Stock Financial Data Extractor

This Python script extracts key financial metrics from a list of specified stocks using the Yahoo Finance API (via `yfinance` library). The script retrieves balance sheet data, ratios, and other stock-related metrics to provide a financial overview of each stock in the list.

## Libraries Required

- **yfinance**: To retrieve stock and financial data from Yahoo Finance.
- **pandas**: For data manipulation and display.

## Getting Started

### Prerequisites

Before running the script, ensure you have the required Python libraries installed:

```bash
pip install yfinance pandas
```

### Usage

1. Modify the `symbols` list in the script to include the stock tickers you want to analyze:
    ```python
    symbols = ['NIO', 'NVDA', 'JNJ', 'TSLA']  # Add/remove tickers as needed
    ```

2. Run the script:
    ```bash
    python stock_data_extractor.py
    ```

### Output Example

```
Stock Information
Ticker: NIO
Total Equity: 5,000,000
Total Liabilities: 10,000,000
```

## License

This project is licensed under the MIT License.
