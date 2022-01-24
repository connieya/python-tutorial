import re

# abcd , book , desk
# ca?e 
# care ,cafe , case , cave


p = re.compile("ca.e") 
# . 는  하나의 문자를 의미한다. 
# ^ 는 문자열의 시작을 의미  (^de) -> desk , destination
# $  는 문자열 의 끝을 의미  (se$) -> case , base

# m = p.match("case")
# print(m.group()) # 매치 되지 않으면 에러가 발생



def print_match(m) :
    if m :
        print("m.group(): " ,m.group()) # 일치하는 문자열 반환
        print("m.string: " ,m.string) # 입력 받은 문자열
        print("m.start(): " ,m.start()) # 일치하는 문자열의 시작 Index
        print("m.end(): " ,m.end()) # 일치하는 문자열 의 끝 
        print("m.span(): " ,m.span()) # 일치하는 문자열 의 시작 /끝  index
    else :
        print("매칭 되지 않음")

# m = p.match("careless")
# print_match(m)        


m = p.search("good care") # search : 주어진 문자열 중에 일치하는 게 있는지 확인
print_match(m)


lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환 
print(lst)