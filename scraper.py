from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to ChromeDriver and headless Chrome binary
driver_path = os.path.join(current_dir, 'drivers', 'chromedriver.exe')  # Path to your ChromeDriver
chrome_path = os.path.join(current_dir, 'drivers', 'chrome-headless-shell-win64', 'chrome.exe')  # Path to headless Chrome

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.binary_location = chrome_path  # Use headless Chrome binary
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Optional: Disables GPU acceleration
chrome_options.add_argument("--window-size=1920,1080")  # Optional: Set window size (useful for scraping)

# Create a Service object for ChromeDriver
service = Service(executable_path=driver_path)

# Set up Selenium WebDriver using the Service object and the headless Chrome options
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the page you want to scrape
url = 'https://www.sick.com/in/en/catalog/products/detection-sensors/photoelectric-sensors/w4/wtb4fp-22161120a00/p/p661408?tab=detail'

# Open the URL in Selenium
driver.get(url)

# Wait for the page to load (adjust the wait time if necessary)
time.sleep(5)

# Try to click the "Accept all cookies" button by its ID
try:
    accept_button = driver.find_element(By.ID, 'gdpr_modal_button_consent')
    accept_button.click()
    print("Clicked 'Accept all cookies'")
except Exception as e:
    print(f"No cookie consent popup found or unable to click: {e}")

# Allow time for the page to reload after accepting cookies
time.sleep(2)

# Get the page source after cookie acceptance
html = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# Function to download the product image
def download_image(soup):
    # Define the folder to store the scraped data
    folder_name = 'scraped-data'
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Define the path where the image will be saved
    image_path = os.path.join(folder_name, 'product-img.jpg')

    image_tag = soup.find('img', {'class': 'block margin-auto loaded'})
    
    if image_tag:
        print("Image tag found: ", image_tag)  # Print the full image tag for debugging
        try:
            # First check for the 'src' attribute
            image_url = image_tag.get('src')
            
            # If 'src' is not present, fall back to 'data-src'
            if not image_url:
                image_url = image_tag.get('data-src')
            
            print("Image URL: ", image_url)
            
            if image_url:
                # Get the image content
                image_data = requests.get(image_url).content
                
                # Save the image in the 'scraped-data' folder
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data)
                
                print(f"Product image saved successfully at {image_path}")
            else:
                print("No image URL found.")
                
        except KeyError:
            print("No 'src' or 'data-src' attribute found in the image tag.")
    else:
        print("Image not found.")


# Download the product image
download_image(soup)

# Close the browser
driver.quit()
