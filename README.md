# Web Scraper for Product Data

This project is a web scraper that extracts data from a specific product page and downloads the product image, technical data in Excel format, and the product data sheet in PDF format. The scraper is built using Python, Selenium, BeautifulSoup, and Flask for the web interface.

## Features
- Scrapes product details like technical specifications and saves them to an Excel file.
- Downloads the product image.
- Downloads the product data sheet in PDF format.
- Provides a web interface for users to enter a product page URL and scrape data.

## Technologies Used
- **Python**: The core programming language used.
- **Selenium**: Used for browser automation to interact with the web page.
- **BeautifulSoup**: Used for parsing the page's HTML and extracting relevant data.
- **Flask**: Provides the web interface for scraping and user interaction.
- **Pandas**: For writing the scraped data into an Excel file.

## Project Structure
```bash
├── app.py # Main Flask application ├── crawler.py # Handles the scraping logic ├── download_product_sheet.py # Handles downloading of the product data sheet ├── templates/ │ └── index.html # HTML template for the web interface ├── static/ │ ├── css/ │ │ └── style.css # CSS styling for the web interface │ ├── images/ │ │ └── web.jpg # Background image │ └── js/ │ └── scripts.js # JavaScript for handling front-end interactions ├── requirements.txt # Python dependencies ├── runtime.txt # Specifies the Python version ├── Procfile # Railway or Heroku deployment settings ├── scraped-data/ # Directory where scraped files are stored │ └── (Excel and PDF files will be saved here) └── .gitignore # Specifies files to be ignored by git
```
## Setup Instructions

### Prerequisites
- Python 3.8 or later
- `pip` (Python package manager)
- Chrome/Chromium Browser
- ChromeDriver (Ensure that you have the correct version of ChromeDriver for your browser version)

### 1. Clone the Repository

```bash
git clone https://github.com/zerreat/your-repo.git
cd your-repo
```