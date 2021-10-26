from random import *

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))

print(int(random() * 45) + 1)  # 1~ 45이하의 임의의 값 생성

print(randrange(1, 46))  # 1~ 46 미만의 임의의 값 생성

print(randint(1, 45))  # 1~ 45이하의 임의의 값 생성


date = randint(4, 28)
