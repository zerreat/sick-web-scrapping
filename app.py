from flask import Flask, request, render_template, send_from_directory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from bs4 import BeautifulSoup
from accept_cookie import accept_cookies
from scrape_image import download_image
from scrape_tables import save_tables_to_excel
from scrape_data_sheet import download_data_sheet  # Importing the new module for data sheet
import zipfile

app = Flask(__name__)

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to ChromeDriver and headless Chrome binary
driver_path = os.path.join(current_dir, 'drivers', 'chromedriver.exe')
chrome_path = os.path.join(current_dir, 'drivers', 'chrome-headless-shell-win64', 'chrome.exe')

@app.route('/')
def index():
    return render_template('index.html', error=None, success=None, download_link=None)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', error="No URL provided", success=None, download_link=None)

    folder_name = 'scraped-data'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)
        accept_cookies(driver)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        # Download product image and scrape table data
        download_image(soup, folder_name)
        save_tables_to_excel(soup, folder_name)

        # Download product data sheet
        download_data_sheet(driver, folder_name)

        # Create zip file containing the scraped data
        zip_filename = 'scraped-data.zip'
        zip_filepath = os.path.join(current_dir, zip_filename)
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            zipf.write(os.path.join(folder_name, 'product-img.jpg'), 'product-img.jpg')
            zipf.write(os.path.join(folder_name, 'product-table.xlsx'), 'product-table.xlsx')
            # Check if the product data sheet exists before adding it to the zip
            if os.path.exists(os.path.join(folder_name, 'product-data-sheet.pdf')):
                zipf.write(os.path.join(folder_name, 'product-data-sheet.pdf'), 'product-data-sheet.pdf')
            else:
                print("Product data sheet not found, skipping zip.")
    finally:
        driver.quit()

    # Render the page with the success message and download link
    return render_template('index.html', 
                           error=None, 
                           success="Your files are ready to download.", 
                           download_link="/download/zip")

@app.route('/download/zip')
def download_zip():
    zip_filepath = os.path.join(current_dir, 'scraped-data.zip')
    return send_from_directory(current_dir, 'scraped-data.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
