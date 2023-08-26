# NepStocks-D-Miner

NepStocks-D-Miner is a Python script designed to extract essential stock data from the Nepal Share Market website for enhanced investment analysis. The script uses web scraping techniques to gather information about various stocks and saves it in an Excel file.

## Features

- Scrapes stock data for a list of specified stock symbols from the Nepal Share Market website.
- Extracts details such as Symbol, Company, Sector, Listed Shares, Paidup Value, Total Paidup Value, Eps, and EPS date.
- Stores the collected data in an Excel file named `StockData.xlsx`.
- Appends new data to an existing Excel file if it already exists.
- Utilizes libraries like `requests`, `BeautifulSoup`, and `pandas` for web scraping and data manipulation.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `BeautifulSoup`, `pandas` and other mentioned in requirement.txt file

## Usage

1. Clone this repository or download the `NepStocks-D-Miner.py` script.
2. Install the required Python packages using the following command:
   ```bash
   pip install requests beautifulsoup4 pandas
other requirements are mentioned in requirement.txt file 
