cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet)
print(cabinet[100])
print(cabinet.get(3))

# none
print(cabinet.get(5))
print("hi")

# 에러

# print(cabinet[5])
print("hi")

print(cabinet.get(5, "사용가능"))
print(3 in cabinet)