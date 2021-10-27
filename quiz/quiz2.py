from random import *

users = range(1,21)
print(type(users))

users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("__ 당첨자 발표 __")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))