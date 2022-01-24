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
print(cartoons[0])
title = cartoons[0].a.get_text()
print(title)
link = cartoons[0].a["href"]
print("https://comic.naver.com"+link)