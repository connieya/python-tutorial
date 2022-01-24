from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta # 'dbsparta'라는 이름의 db를 만듭니다.
# print(client)
# print(client.list_database_names())

# 코딩 시작
# user 라는 collection 에 데이터 넣기
# db.users.insert_one({'name' : 'bobby' , 'age' : 21})
# db.users.insert_one({'name' : 'kay' , 'age' : 27})
# db.users.insert_one({'name' : 'john' , 'age' : 30})

# all_users = list(db.users.find({}))
# print(all_users)

same_ages = list(db.users.find({'age':21}))

print(same_ages)

# db.users.update_one({'name':'bobby'},{'$set':{'age':59}})

# user = db.users.find_one({'name':'bobby'})
# print(user)

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)