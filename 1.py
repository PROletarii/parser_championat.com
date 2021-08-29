import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://www.championat.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html,team_name):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='article-preview')
    articles = []
    for item in items:
        title = item.find('a', class_='article-preview__title').get_text(strip=True)
        link = item.find('a', class_='article-preview__title').get("href")
        if team_name in str(title):
            print(title)
            print(HOST + link)
            print("=================")
        articles.append({
            'title': item.find('a', class_='article-preview__title').get_text(strip=True),
            "link":  HOST + soup.find('a', class_='article-preview__title').get("href"),
            #'usd_price': item.find('span', class_='green').get_text(strip=True),
            #'uah_price': uah_price,
            #'city': item.find('span', class_='item region').get_text(strip=True),
        })
    #print(*articles, sep='\n')
    #print(len(articles))

    return articles


def parse():
    count = 1
    team_name = input('Введите название команды - ')
    while True:
        URL = f'https://www.championat.com/articles/football/_russiapl/{count}.html'
        html = get_html(URL)
        if html.status_code == 200:
            articles = get_content(html.text, team_name)
            count += 1
        else:
            print('Error')



parse()
