import re
import requests
import sqlite3
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_html(url):
    try:
        response = requests.get(url)
        html = response.text
    except Exception as error:
        print(f"Открыть страничку по адрессу {url}, неудалось. Ошибка: {error}")
    return html


def parse_roskosmos_news():
    base_url = 'https://www.roscosmos.ru/102/'
    news_list_html = get_html(base_url)
    soup = BeautifulSoup(news_list_html, "html.parser")
    mounth_news = []
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if re.fullmatch('/102/\d{6}/', href):
            mounth_news.append('https://' + urlparse(base_url).netloc + href)

    news_head = []
    for url_mounth_news in mounth_news:
        page_news = get_html(url_mounth_news)
        soup = BeautifulSoup(page_news, "html.parser")
        for tag_news in soup.findAll(class_="newslist"):
            news_name = tag_news.find(class_="name").text
            news_head.append(news_name)
    print(f'На сайте roskosmos найдено {len(news_head)} новостей.')
    return news_head


def write_db(news_list):
    try:
        conn = sqlite3.connect('roskosmos_news.db')
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS roskosmos_news (
        id_news INTEGER PRIMARY KEY AUTOINCREMENT,
        news_name varchar(150)
        );
        """)
        conn.commit()
        for news in news_list:
            print(news)
            cur.execute("INSERT INTO roskosmos_news VALUES(?, ?);", (None, news))
            conn.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")


def main():
    news_list = parse_roskosmos_news()
    write_db(news_list)
    print('В БД roskosmos_news.db успешно записаны заголовки новостей')


if __name__ == "__main__":
    main()
