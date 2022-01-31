import requests
from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday"
url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text , "lxml")

# cartoons = soup.find_all("a", attrs ={"class" : "title"})

# for cartoon in cartoons :
#     print(cartoon.get_text())
cartoons = soup.find_all("td", attrs = {"class" : "title"})
# print(cartoons[0])
title = cartoons[0].a.get_text()
# print(title)
link = cartoons[0].a["href"]
# print("https://comic.naver.com"+link)

# gaoos = soup.select("#container > #content > table > tr >  td:nth-child(2) > a")
gaoos = soup.select("#container > #content > table > tr")
# print(gaoos)
#content > table > tbody > tr:nth-child(1) > td:nth-child(1) > a


for g in gaoos:
    if g is not None :
       rate = g.find("strong").get_text();
       title = g.select_one("td:nth-child(2) > a").text
    print(title, " : " , rate)