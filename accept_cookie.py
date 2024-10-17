from selenium.webdriver.common.by import By

def accept_cookies(driver):
    """
    Function to click the 'Accept all cookies' button.
    """
    try:
        accept_button = driver.find_element(By.ID, 'gdpr_modal_button_consent')
        accept_button.click()
        print("Clicked 'Accept all cookies'")
    except Exception as e:
        print(f"No cookie consent popup found or unable to click: {e}")
