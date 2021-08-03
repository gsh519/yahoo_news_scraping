import csv
from PIL.Image import new
import requests
from bs4 import BeautifulSoup
from requests.api import get

HEADER = ['ニュース', 'URL'] # 追加部分

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)

# html取得
soup = BeautifulSoup(res.text, 'html.parser')


spot = soup.find('div', attrs={'class': '_2jjSS8r_I9Zd6O9NFJtDN-'})

# 更新日取得
update_time = spot.find('p').text
# print(update_time)

data = []
li_tags = spot.find_all('li', attrs={'class': '_2j0udhv5jERZtYzddeDwcv'})
with open('Yahoo_news.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for li_tag in li_tags:
        
        # テキスト取得
        news_text = li_tag.find('span', attrs={'class': 'fQMqQTGJTbIMxjQwZA2zk'}).text
        
        # URL取得
        news_url = li_tag.find('a', attrs={'class': 'yMWCYupQNdgppL-NV6sMi'})['href']
        
        row = [news_text, news_url]
        writer.writerow(row)

import pandas as pd
df = pd.read_csv('Yahoo_news.csv')
print(df)






