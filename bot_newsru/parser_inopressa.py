from bs4 import BeautifulSoup as bs
import requests


def parser():
    """
    Функция парсит новостные данные с сайта
    :return: dict
    """
    response = requests.get(URL_HOST, HEADER)
    soup = bs(response.content, 'html.parser')
    items = soup.findAll('div', class_='topnews')
    data = []
    for item in items:
        data.append({
            'title': item.find('a', tag='h3').get_text(strip=True),
            # 'description': item.find('a', class_='lead').get_text(strip=True),
            # 'link': URL + item.find('a', class_='lead').get('href')
        })
    return data, items


# def list_compilation(data):
#     res = 0
#     data_set = []
#     for news in data:
#         res += 1
#         item = f"{res} - - - - - - - - \n" \
#                f"{news['title']}\n" \
#                f"{news['description']}\n" \
#                f"{news['link']}\n"
#         data_set.append(item)
#         if res == 10:
#             break
#     # acc_string = '\n'.join(data_set)
#     return data_set


URL_HOST = 'https://www.inopressa.ru/'
URL = 'https://www.inopressa.ru/'
HEADER = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'

data = parser()
print(data)
# info = list_compilation(data)