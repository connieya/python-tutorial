from email import header
from http import client
from wsgiref import headers
from markupsafe import re
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.dbjungle

# DB에 저장할 영화인들의 출처 url 
def get_urls() :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text , 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')
    
    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)
            
    return urls        

def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text , 'html.parser')
    info_area = soup.select_one('#content > div.article > div.mv_info_area')
    name = info_area.select_one('div.character > h3 > a').text
    img_url = info_area.select_one('div.poster > img')['src']
    work = info_area.select_one('div.character > dl > dd > a:nth-child(1)').text
    doc = {
        'name' : name,
        'img_url' : img_url,
        'recent' : work,
        'url' : url,
        'like' : 0
    }
    db.mystar.insert_one(doc)
    print('완료!',name)
    
    


def insert_all():
    db.mystar.drop()
    urls = get_urls()
    for url in urls:
        insert_star(url)
     
insert_all()
# insert_star('https://movie.naver.com//movie/bi/pi/basic.naver?st=1&code=1540')