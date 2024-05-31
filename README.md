
# Scrape filter name and their option from website

Scrape all filter titles and their options from the given webpage in English. Store the scraped data in an Excel sheet with separate columns for the filter title and its options.


## Tech Stacks

- requests: For sending HTTP requests.
- BeautifulSoup: For parsing HTML and extracting data.
- pandas: For manipulating data and saving it to an Excel file.
- selenium: Used for automating web browsers.

## Prerequisites
Ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas selenium

```

## Features
- Data Extraction: Extracts filter titles and their corresponding options from the web page. Handles HTML structures to accurately identify and parse filter sections.
- Data Storage in Excel: Utilizes pandas to organize extracted data into a structured format. Saves the extracted data into an Excel file using openpyxl.

## Functionality:
- Initializes a web driver to load the webpage.
- Extracts text data from specified HTML elements.
- Handles interaction with elements, including clicking and navigating.
- Cleans and processes the extracted data.
- Saves the data into a CSV file for further analysis or use.

## Setup and Installation

- Clone the repository.
- Navigate to the project directory.
- Install required dependencies.
- Run the app.

```bash
py filter_extraction.py
```










## Used By

- Academic Projects: Students or researchers might use this script to gather data for a thesis or project, analyzing how different attributes affect car pricing and availability.
- Market Researchers: Researchers conducting a study on the automotive market could use this to collect data on car listings, filtering options, and attributes like year, price, and mileage from websites like Syarah.




## 🚀 Conclusion

In conclusion, this project serves as a solid foundation for web scraping tasks using Selenium. It demonstrates how to automate interactions with web pages and extract useful data, which can be further analyzed to derive insights.

## Support

For support, email pratikshagarkar871999@gmail.com


## About me

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@pratiksha.garkar)

