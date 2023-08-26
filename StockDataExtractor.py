import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pathlib import Path


excelPath = Path(r'C:\Users\sanja\OneDrive\Desktop\NepStocks-D-Miner\StockData.xlsx')

symbol = [  "SHPC", "NICA", "NTC", "SCB", "NABIL", 
    "HBL", "EIC", "UPPER", "NIB", "NBB", 
    "SBL", "PCBL", "SIC", "SANIMA", "MEGA",
    "GBIME", "CBBL", "NIFRA", "PFL", "NIBPO",
    "EDBL", "NLIC", "LICN", "NHPC", "CIT",
    "JOSHI", "NMB", "HAMRO", "API",
    "NRIC"] #Add other stock name to in this list. Might come error if symbol data is not available in site.
for s in symbol:
    url1 = os.environ.get('stockurl')
    mainurl = f'{url1}{s}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    store = requests.get(mainurl, headers=headers)
    soup = BeautifulSoup(store.text, 'html.parser')
    with open("StockData.html", 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    with open("StockData.html", 'r', encoding='utf-8') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'html.parser')
    downa = []
    upa = []
    eps = []
    epsdate = []

    def down():
        downarea = soup.select('div.table-responsive')  # for list select
        for div in downarea:
            tdtag = div.find_all('td')
            for ele in tdtag:
                downa.append(ele.get_text(strip=True))

    def uppereps():
        global epsdate
        uparea = soup.select("tbody.panel.panel-default")
        tdtag = uparea[9].select('td')
        for ep in tdtag:
            tdtag = ep
            tm = tdtag.get_text()
            tdreal = tm.split('''\n            \n             ''')
        epsdate = [item.strip() for item in tdreal]

    down()
    uppereps()

    Info = downa + epsdate
    # print(Info)
    
    if excelPath.exists():
        table = pd.DataFrame([Info], columns=['Symbol', 'Company', 'Sector', 'Listed Shares', 'Paidup Value', 'Total Paidup Value', 'Eps', 'EPS date'])
        
        # Read the existing data
        old = pd.read_excel('StockData.xlsx')
        
        # Concatenate and overwrite the existing file
        new_data = pd.concat([old, table], ignore_index=True)
        new_data.to_excel('StockData.xlsx', index=False)
        
    else: 
    
        table = pd.DataFrame([Info], columns=['Symbol', 'Company', 'Sector', 'Listed Shares', 'Paidup Value', 'Total Paidup Value', 'Eps', 'EPS date'])

        # Write the new data to a new Excel file
        table.to_excel('StockData.xlsx', index=False)

print("Data appended and saved successfully!")




    
# downa.append(td_content_cleaned)
# print(tdtag.get_text())


# for td in tdtag:
#     if not ('text-primary') in td.get('class'):
#         eps.append(td.get_text(strip=True))
    
# # upp = uparea.select('tbody')
# # up2 = upp.find(class_='')
# print(eps)

# for tdt in uparea:
#     tadtag = tdt.select('td')
# print(tadtag)
    # for tdtag in tadtag:
        # print(tdtag.get_text(strip=True))
# print(tadtag.string)


# for downarea in downarea:
#     print(downarea.find('td').get_text())

# print(symbol)






# print(downa)
# print(epsdate)