# site = "http://naver.com"
url = "http://www.google.com"
my_url = url.replace("http://", "")

print(my_url)

index1 = my_url.index(".")
index2 = my_url.index(".", index1+1)

my_url = my_url[index1+1:index2]

password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print(my_url)

print("{0}의 비밀번호는 {1}입니다.".format(url, password))
