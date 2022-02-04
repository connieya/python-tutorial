import requests

from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost',27017)
# client = MongoClient('mongodb://connie:1234@3.37.86.47',27017)
db = client.geonhee
headers = { 
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
def insert_all():
    db.movies.drop()
    url =  "https://movie.naver.com/movie/sdb/rank/rpeople.naver"

    data = requests.get(url, headers = headers)
    soup = BeautifulSoup(data.text , 'html.parser')

    hrefs = soup.select("#old_content > table > tbody > tr > td.title > a")
    for href in hrefs :
        if href is not None :
            base_url = "https://movie.naver.com/"
            url = base_url+ href['href']
            insert_star(url)



def insert_star(url) :
   data = requests.get(url,headers= headers) 
   soup = BeautifulSoup(data.text, 'html.parser')
   name = soup.find("h3",attrs = {"class" : "h_movie"}).a.get_text()
   image_url = soup.select_one("div.article > div.mv_info_area > div.poster > img")['src']
   recent_work = soup.select_one("div.article > div.mv_info_area > div > dl > dd > a")['title']
   doc = {
       'name' : name ,
       'image_url' : image_url,
       'recent_work' : recent_work ,
       'like' : 0
   }
   db.movies.insert_one(doc)
   print('insert 완료 ' , name)



insert_all()