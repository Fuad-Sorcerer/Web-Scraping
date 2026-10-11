# Daraz Earbuds Scraper

A simple Python project that collects earbuds names and prices from Daraz Bangladesh and saves them to a CSV file.

## Features

- Opens Daraz in Chrome using Selenium.
- Extracts product names and prices using BeautifulSoup.
- Displays the results in the terminal.
- Saves the data to `earbus.csv`.

## Requirements

- Python 3
- Google Chrome
- Internet connection

Install the required packages:

```bash
python -m pip install selenium beautifulsoup4
```

The `csv` module comes with Python. No installation is needed for it.

## How to Run

1. Download this project's Python file.
2. Open its folder in VS Code.
3. Run the Python file.
4. Wait until product names and prices appear in the Chrome window.
5. Return to the VS Code terminal and press **Enter**.
6. The script will extract the data, save the CSV file, and close Chrome.

## Output

The script creates `earbus.csv` in the terminal's current folder.

Example output:

| name | price |
| --- | --- |
| Example Earbuds A | ৳ 399 |
| Example Earbuds B | ৳ 309 |

Open the CSV file in Excel to see the data in separate columns.

**Running the script again overwrites the existing CSV file when product boxes are found.**

## How It Works

1. **Selenium** opens the website in Chrome.
2. **BeautifulSoup** reads the loaded HTML.
3. **`find_all()`** finds the product boxes.
4. A **`for` loop** extracts each product's name and price.
5. **`csv.writer()`** writes the results to the CSV file.

## Limitations

- Collects matching products from the currently loaded page only.
- Does not automatically scroll or visit additional pages.
- Skips products when the name or price tag is missing.
- Website changes may require updates to the selectors.
- Prices are saved as text, including the currency symbol.

## Author

Mofasser Ahmed Fuad

Created as a Python web scraping practice project.
