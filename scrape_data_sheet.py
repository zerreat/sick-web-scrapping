import os
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_data_sheet(driver, folder_name):
    """Download the product data sheet from the given page using Selenium."""
    
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Define the path for saving the product data sheet
    data_sheet_path = os.path.join(folder_name, 'product-data-sheet.pdf')
    
    try:
        # Wait for the download button to be clickable
        data_sheet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='action-button flex-grow font-bold']"))
        )
        
        # Click the "English" button
        data_sheet_button.click()
        time.sleep(2)  # Wait for the link to appear

        # Find the download link for the Product Data Sheet
        data_sheet_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.sick-icon-download"))
        ).get_attribute("href")

        # Download the data sheet PDF
        data_sheet_response = requests.get(data_sheet_link)
        with open(data_sheet_path, 'wb') as f:
            f.write(data_sheet_response.content)

        print(f"Product data sheet downloaded successfully at {data_sheet_path}")

    except Exception as e:
        print(f"Error downloading product data sheet: {e}")
    
    return data_sheet_path
