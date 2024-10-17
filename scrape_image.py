import os
import requests
from bs4 import BeautifulSoup

def download_image(soup, folder_name):
    """
    Function to download the product image and save it in the 'scraped-data' folder.
    """
    image_path = os.path.join(folder_name, 'product-img.jpg')

    image_tag = soup.find('img', {'class': 'block margin-auto loaded'})
    
    if image_tag:
        try:
            image_url = image_tag.get('src') or image_tag.get('data-src')
            if image_url:
                image_data = requests.get(image_url).content
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data)
                print(f"Product image saved successfully at {image_path}")
            else:
                print("No image URL found.")
        except KeyError:
            print("No 'src' or 'data-src' attribute found in the image tag.")
    else:
        print("Image not found.")
