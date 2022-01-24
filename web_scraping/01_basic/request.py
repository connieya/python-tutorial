import imp


import requests
res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")
res = requests.get("http://google.com")
# print(res.status_code)

res.raise_for_status()
if(res.status_code == requests.codes.ok) :
    print('정상 입니다.')
    
else:
    print("문제가 생겼습니다. 에러코드  = ",res.status_code)

# print(len(res.text))
# print(res.text)

with open("mygoogle.html","w",encoding="utf-8") as f:
    f.write(res.text)