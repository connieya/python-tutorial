# 1. pymongo 패키지 설치

# 2.  DB 연결하기 

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 3. 데이터 넣기
# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})


# 4.모든 결과 값을 보기
# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))
# print(all_users)


# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':21}))
# print(same_ages)

# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    # print(user)

# 5. 특정 결과 값을 뽑아 보기
u = db.users.find_one({'name':'bobby'})
# print(u)

# 그 중 특정 키 값을 빼고 보기
u = db.users.find_one({'name':'bobby'},{'_id':False})  # _id 값 빼고 출력하기
# print(u)

# 6.  수정하기
# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })

# 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# user = db.users.find_one({'name':'bobby'})
# print(user)


# 7. 삭제하기
# db.users.delete_one({'name':'bobby'})
db.users.delete_many({'name':'john'})

# user = db.users.find_one({'name':'boby'})
# print(user)