import os
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_data_sheet(driver, folder_name):
    """Download the product data sheet from the given page using Selenium."""
    
    # Define the path for saving the product data sheet
    data_sheet_path = os.path.join(folder_name, 'product-data-sheet.pdf')
    
    try:
        # Locate and click the button for the data sheet in English
        data_sheet_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(),'English')]]"))
        )
        data_sheet_button.click()
        print("Clicked on 'English' button for data sheet.")

        time.sleep(2)  # Wait for the new tab to load

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched to new tab.")

        # Wait for the PDF URL to load in the address bar
        WebDriverWait(driver, 15).until(EC.url_contains(".pdf"))
        pdf_url = driver.current_url

        print(f"PDF URL found: {pdf_url}")  # Debugging output

        # Validate that the URL ends with .pdf
        if not pdf_url.lower().endswith('.pdf'):
            raise ValueError("The URL does not point to a valid PDF.")

        # Download the PDF using requests with User-Agent header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        data_sheet_response = requests.get(pdf_url, headers=headers)

        # Check for a successful response
        if data_sheet_response.status_code == 200:
            with open(data_sheet_path, 'wb') as f:
                f.write(data_sheet_response.content)
            print(f"Product data sheet downloaded successfully at {data_sheet_path}")
        else:
            raise Exception(f"Failed to download PDF. HTTP Status Code: {data_sheet_response.status_code}")

        # Close the new tab and switch back to the original tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Closed new tab and switched back to original tab.")
    
    except Exception as e:
        print(f"Error downloading product data sheet: {e}")
    
    return data_sheet_path
