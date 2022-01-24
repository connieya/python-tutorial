from attr import attr, attrs
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
print("***** 웹 스크래핑 시작 *******")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a.attrs)
# print(soup.a["href"])
# print(soup.find("a",attrs = {"class": "Nbtn_upload"}))
# print(soup.find("li",attrs={"class" : "rank01"}))

rank01 = soup.find("li",attrs={"class" : "rank01"})

print(rank01.a.get_text())
# print(rank01.next_sibling.next_sibling)
# rank02 = rank01.next_sibling.next_sibling
# print(rank02.get_text())
# rank03 = rank02.previous_sibling.previous_sibling
# print(rank03.get_text())
# print(rank01.parent)
# rank02 = rank01.find_next_sibling("li")
# print(rank02.get_text())

print("******* 모든 형제  출력 ****")
siblings = rank01.find_next_siblings("li")
# print(siblings)


