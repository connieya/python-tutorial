from ctypes import c_uint

customer = "토르"

index = 5

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
#     index += 1


# customer = "베트맨"
#
# person = "Unknown"
#
# while person != customer :
#     print("{0},  커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# continue , break


absent = [2, 5]  # 결석
no_book = [7]

for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기 까지 . {0}는 교무실로 따라와라".format(student))
        break

    print("{0}, 책을 읽어봐".format(student))




students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron Man" , "Thor" , "I am groot"]
students = [len(i) for  i in students]
print(students)
students = ["Iron Man" , "Thor" , "I am groot"]
students = [ i.upper() for i in students]
print(students)