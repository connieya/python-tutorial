from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbjungle                     # 'dbsparta'라는 이름의 db를 만듭니다.


result = db.movies.find({})
# db.movies.insert_one({'rank' : 51 ,'title':'매트릭스','star':9.33})



#  db에 있는 제목들 추출하기 

# print("***************** DB에 있는 모든 영화 **************")
# for res in result :
#     print(res['title'])

# print("************************ 특정 영화 평점 검색 **************")
# target_movie = db.movies.find_one({'title':'매트릭스'})

# print(target_movie['star'])

# star = target_movie['star']


# print("************** 매트릭스 평점과 같은 영화들 **************")

# movies = list(db.movies.find({'star': star}))

# for movie in movies :
#     print(movie['title'])


print("*********** 매트릭스 평점 변경하기 ***********")

db.movies.update_one({'title':'매트릭스'},{'$set' : {'star':9.80}})