import requests
from bs4 import BeautifulSoup as bs
import xlsxwriter

url = 'https://parsemachine.com/sandbox/catalog/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36'}
data = [['Название']]
page = 1

while True:
    url_with_page = f"{url}?page={page}"
    try:
        res = requests.get(url_with_page)
        res.raise_for_status()  # Проверка успешности запроса
        html = bs(res.content, 'html.parser')
        items = html.findAll('div', class_='row mt-3')

        for el in items:
            for a in el.findAll('div', class_='card-body'):
                title = el.find('h6', class_='card-title').text
                data.append([title])
        page += 1

    except:
        break

with xlsxwriter.Workbook('shop.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, info in enumerate(data):
        worksheet.write_row(row_num, 0, info)










