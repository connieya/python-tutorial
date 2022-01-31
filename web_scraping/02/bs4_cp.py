from attr import attrs
import requests
import  re
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

for i in range(1,6) : # 쿠팡 페이지 1~5페이지
    print("페이지 : " ,i);
    url = "https://www.coupang.com/np/search?rocketAll=false&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=5581323&component=&rating=0&sorter=scoreDesc&listSize=36".format(i)
    
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.find_all("li" , attrs={"class" : re.compile("^search-product")})
    items[0].find("div", attrs = {"class" : "name"}).get_text()
    # print(items)
    for item in items :
        # 광고 제품은 제외
        link = item.find("a" , attrs = {"class" : "search-product-link"})["href"]
        ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
        if ad_badge :
            # print("광고 제품 제외합니다.")
            continue
        
        i = item.select_one("li > a > dl > dd > div")
        name = i.find("div", attrs = {"class" : "name"}).get_text()

        # 애플 제품 제외
        if "Apple" in name :
            # print("Apple 상품 제외합나다.")
            continue
    
        price = i.find("strong", attrs = {"class" : "price-value"}).get_text()
        # price = i.select_one("div.price-area > div.price-wrap > div.price > em > strong").get_text()
        rate = i.find("em", attrs = {"class" : "rating"})
        if rate :
            rate = rate.get_text()
        else :
            rate = "평점 없음"
            # print("평점 없는 상품은 제외합니다.")
            continue
        rate_cnt = i.find("span", attrs = {"class" : "rating-total-count"})
        if rate_cnt :
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[ 1:-1]
        else :
            rate_cnt = "평점 없음"
            # print("평점 없는 상품은 제외합니다.")
            continue

        # 평점이 4.5 이상  리뷰가 50개 이상인 상품만 출력
        if float(rate) >= 4.5 and int(rate_cnt) >= 50 :
            print(f"제품명 : {name}")
            print(f"가격 : {price}원")
            print(f"평점 : {rate} , 평점 수 : {rate_cnt}")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100) # 줄 긋기
