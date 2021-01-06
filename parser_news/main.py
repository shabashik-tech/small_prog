from bs4 import BeautifulSoup as bs
import requests

news_file_name = 'newsru.txt'
URL_HOST = 'http://txt.newsru.com/allnews/'
URL = 'http://txt.newsru.com'
HEADER = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'

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

with open(news_file_name, 'w', encoding='utf-8') as file:
    for news in data:
        item = (f"{news['title']}\n{news['description']}\n{news['link']}\n\n")
        file.write(item)