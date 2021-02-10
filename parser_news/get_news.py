from bs4 import BeautifulSoup as bs
import requests


def parser():
    """
    Функция парсит новостные данные с сайта
    :return: dict
    """
    response = requests.get(URL_HOST, HEADER)
    soup = bs(response.content, 'html.parser')
    items = soup.findAll('table', class_='index-news-item')
    data = []
    for item in items:
        data.append({
            'title': item.find('a', class_='index-news-title').get_text(strip=True),
            'description': item.find('a', class_='index-news-text').get_text(strip=True),
            'link': URL + item.find('a', class_='index-news-text').get('href')
        })
    return data


def save_file(data):
    """
    Функция сохраняющая данные переданные парсером
    :param data: dict
    """
    with open(NEWS_FILE_NAME, 'w', encoding='utf-8') as file:
        res = 0
        for news in data:
            res += 1
            item = f"{res} - - - - - - - - \n" \
                   f"{news['title']}\n" \
                   f"{news['description']}\n" \
                   f"{news['link']}\n\n"
            file.write(item)


NEWS_FILE_NAME = 'newsru.txt'
URL_HOST = 'http://txt.newsru.com/allnews/'
URL = 'http://txt.newsru.com'
HEADER = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'


def main():
    data = parser()
    save_file(data)


if __name__ == '__main__':
    main()
