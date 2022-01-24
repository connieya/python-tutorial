from ast import If
import re


people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27},
          {'name': 'cony' , 'age' : 29}]



for p in people :
    print(p['name'] , p['age'])


print('*********** 함수 만들기 *************')


def get_age(name) :
    for person in people:
        if(person['name'] == name) :
            return person['age']    
    return '해당 이름이 존재하지 않습니다.'    

  

result = get_age('ben')
print(result)
print(get_age('거니'))
print(get_age('cony'))
print(get_age('carry'))