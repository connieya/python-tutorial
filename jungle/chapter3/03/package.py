import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

print(r)

rjson = r.json()

# print(rjson)

mise = rjson["RealtimeCityAir"]
# print(mise)
mise = mise["row"]
# print(mise)

# for m in mise :
#     print(m['MSRSTE_NM'], m['IDEX_MVL'])


for gu in mise :
    if gu['IDEX_MVL'] <= 60 :
        print(gu['MSRSTE_NM']," : ", gu['IDEX_MVL'])    