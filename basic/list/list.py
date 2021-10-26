# 리스트 []

# 지하철 칸별로 10명 ,20명 , 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석" , "조세호" , "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")

print(subway)

subway.insert(1 , "정형돈")
print(subway)

# 빼기

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 인지
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


# 정렬도 가능

num_list = [4,3,2,1,6,5]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용

mix_list = ["조세호" , 20 , True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)