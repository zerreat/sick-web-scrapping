# Web Scraper

This project is a Flask-based web scraper that fetches product details, images, and product sheet PDFs from specified URLs. 

## Prerequisites

Before you can run the program locally, you need to have the following installed on your machine:

- **Python 3.6 or higher**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Pip**: The package installer for Python should be included with your Python installation. You can check if it is installed by running `pip --version` in your command prompt or terminal.

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone <repository-url>
cd web-scraper
```

### 2. Create a Virtual Environment

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
```bash
venv\Scripts\activate
```

- **macOS/Linux**:
```bash
source venv/bin/activate
```

### 3. Install Required Packages

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Download Chrome WebDriver and Chrome

To run the program, you need to download the Chrome WebDriver and the Chrome executable:

1. Download the **Chrome WebDriver** from [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads).
2. Download the **Chrome executable** from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable).

### 5. Save the Executables

Save the downloaded files to the appropriate directories:

- Place the Chrome WebDriver executable in the `drivers/` directory and rename it to `chromedriver.exe`:

```bash
drivers/chromedriver.exe
```

- Place the Chrome executable in the `drivers/chrome-win64/` directory and rename it to `chrome.exe`:

```bash
drivers/chrome-win64/chrome.exe
```

### 6. Run the Program

Now you can run the Flask application:

```bash
python app.py
```

### 7. Access the Application

Open your web browser and go to:

```
http://127.0.0.1:5000
```

### Functionality

The application allows you to enter a product URL, and it will fetch the following:

- Product details
- Product image
- Product sheet PDF

### Notes

- Ensure that the Chrome browser version matches the Chrome WebDriver version for compatibility.
- If you encounter any issues, make sure the paths in your `.gitignore` and other configurations are correctly set.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
