import os
import pandas as pd
from bs4 import BeautifulSoup

def scrape_table(soup, panel_id):
    """
    Scrape table data for a given panel by its id.
    """
    table_data = []
    panel_div = soup.find('div', {'id': panel_id})
    if panel_div:
        table = panel_div.find('div', {'class': 'tech-table'}).find('table')
        if table:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 2:  # Ensure we have key-value pairs
                    key = columns[0].text.strip()
                    value = columns[1].text.strip()
                    table_data.append({"Key": key, "Value": value})
    return table_data

def save_tables_to_excel(soup, folder_name):
    """
    Scrape tables for each panel and save the data into an Excel file.
    """
    panels = [
        {"id": "panel-Features", "name": "Features"},
        {"id": "panel-Safety-related parameters", "name": "Safety-related parameters"},
        {"id": "panel-Communication interface", "name": "Communication interface"},
        {"id": "panel-Electrical data", "name": "Electrical data"},
        {"id": "panel-Mechanical data", "name": "Mechanical data"},
        {"id": "panel-Ambient data", "name": "Ambient data"},
        {"id": "panel-Smart Task", "name": "Smart Task"},
        {"id": "panel-Diagnosis", "name": "Diagnosis"},
        {"id": "panel-Certificates", "name": "Certificates"},
        {"id": "panel-Classifications", "name": "Classifications"}
    ]

    data_dict = {}
    for panel in panels:
        table_data = scrape_table(soup, panel['id'])
        if table_data:
            df = pd.DataFrame(table_data)
            data_dict[panel['name']] = df
        else:
            print(f"No data found for panel {panel['name']}")

    excel_file_path = os.path.join(folder_name, 'product-table.xlsx')
    
    if os.path.exists(excel_file_path):
        os.remove(excel_file_path)

    with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
        for sheet_name, df in data_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Data saved to {excel_file_path}")
