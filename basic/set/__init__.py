# 집합 (set)
# 중복 안됨 , 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

java = {"유재석" , "김태호" , "양세형"}
python = set(["유재석" , "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합

print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 파이썬 은 할 줄 모르느 개발자

print(java-  python)
print(java.difference(python))

python.add('김태호')
print(python)

java.remove("김태호")
print(java)