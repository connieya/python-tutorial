from random import *

cnt = 0
for i in range(1, 51):  # 1 ~ 50 이라는 수
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분".format(i, time))


print("매칭 수 : {0}명".format(cnt))