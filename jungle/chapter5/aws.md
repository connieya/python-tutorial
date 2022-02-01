# 서버 세팅

https://wookim789.tistory.com/34

## putty 로 서버 접속하기

인프런 - Putty를 통한 EC2 접속

https://www.inflearn.com/course/aws-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%9D%B8%ED%94%84%EB%9D%BC-%EA%B8%B0%EB%B3%B8/lecture/54499?tab=note&volume=1.00&speed=1.75




## 서버 실행하기

패키지 설치를 도와줄 패키지 , pip 설치하기

```shell
# pip3 설치
sudo apt-get update
sudo apt-get install -y python3-pip

# 버전 확인
pip3 --version

# pip3 대신 pip 라고 입력하기 위한 명령어
# 아래 명령어를 입력하면 pip 라고 쳐도 pip3를 작동시킬 수 있습니다.
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
```

설치한 pip를 이용해 flask 설치

```shell
pip install [패키지 이름]
pip install flask
```

### AWS 에서 5000 포트 열어주기
세 가지 포트를 추가해봅니다. (80, 5000포트는 미리 추가해두겠습니다)

→ 5000포트: flask 기본포트

→ 80포트: HTTP 접속을 위한 기본포트

→ 27017포트: 외부에서 mongoDB 접속을 하기위한 포트




## 서버에 DB 세팅

mongoDB 설치하기

```shel
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org
```

mongoDB 실행하기

- EC2 에 접속한 터미널(윈도우즈는 GitBash) 에 아래와 같이 입력합니다.
- 실행. 아무 반응이 없으면, 잘 실행된 것! 리눅스는 보통 잘 되면 아무것도 안나옵니다.


```shell

sudo service mongod start
```


우리가 만든 mongoDB를 외부 접속할 수 있게 하기 위해,
접속에 필요한 아이디와 비밀번호를 세팅해보자
설정을 하지 않으면 누구나 DB 정보를 볼 수 있다.

### mongoDB 접속 계정 생성하기

```shell
# mongoDB 쉘에 들어가기
mongo
```

<aside>
👉 좌측에 '>' 표시가 나오면 성공적으로 MongoDB에 접속한 것입니다! 다음 명령어를 순차적으로 입력해주세요.

눈치채셨겠지만,
test, test 자리에 내가 넣고 싶은 아이디/비밀번호를 넣으면 됩니다. (영어만 가능)

</aside>

```shell
# admin으로 계정 바꾸기
use admin;

# 계정 생성하기
db.createUser({user: "test", pwd: "test", roles:["root"]});
```

```shell
# mongoDB 쉘에서 나오기
exit

# MongoDB 재시작
sudo service mongod restart
```

## mongoDB를 외부에 열어주기 - mongoDB 설정 업데이트

mongoDB는 기본적으로 같은 IP 안에서만 접속을 허용하고 있습니다.
앞으로 할 것은 외부에서 접근이 가능하도록 잠금을 풀어주는 작업입니다.

mongoDB는 디폴트로 내부에서만 접속을 허용하고 있습니다. 이 작업은 외부에서 접근이 가능하도록 잠금을 풀어주는 것입니다.

```shell
sudo vi /etc/mongod.conf

# sudo: 관리자(SuperUser) 권한으로 다음을 실행
# vi: 리눅스에서 VS Code 대신 사용하는 텍스트에디터인 Vim을 실행
# => "관리자 권한으로 /etc 폴더 아래 mongod.conf 파일을 Vim으로 켜줘!"라는 뜻입니다
```


```shell
net :
    port : 27017
    bindIp : 127.0.0.1 => 0.0.0.0


#security  :
    authorization : enabled 추가

```



```shell
# 내용 저장하고 에디터 종료하기. esc 누르고 다음 입력.
:wq

# 재시작
sudo service mongod restart
```

## 06.서버 완성

### 포트 포워딩

포트 번호 없애기 - 기본 개념

- 지금은 5000 포트에서 웹 서비스가 실행되고 있습니다. 그래서 매번 :5000 이라고 뒤에 붙여줘야 하죠
- http 요청에서는 80포트가 기본이기 때문에, 굳이 :80을 붙이지 않아도 자동으로 연결이 됩니다.
- 포트 번호를 입력하지 않아도 자동으로 접속되기 위해, 우리는 80포트로 오는 요청을 5000포트로 전달하게 하는 포트포워딩(port forwarding ) 을 사용하겠습니다.
- 리눅스엣거 기본으로 제공해주는 포트포워딩을 사용할 것입니다. 

포트 번호 없애기 - 리눅스 자체 포트포워딩을 작동시키기

- 터미널에서 새롭게 설정을 적용하기 전에 돌아가고 있던 서비스는 중지해야함 (Ctrl + C)
- 포트포워딩 룰 입력

```shell
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
```


### nohup 설정

git bash 또는 맥의 터미널을 종료하면 (SSH 접속을 끊으면) 프로세스가 종료되면서, 
서버가 돌아기지 않는다. 원격 접속을 끊어도, 서버는 계속 동작해야 함

- 원격 접속을 종료하더라도 서버가 계속 돌아가게 하기
  
```shell
nohup python app.py &
```

- 서버 종료하기 - 강제 종료하는 방법

```shell
# 아래 명령어로 미리 pid 값(프로세스 번호)을 본다
ps -ef | grep 'app.py'

# 아래 명령어로 특정 프로세스를 죽인다
kill -9 [pid값]
```

- 다시 켜기

```shell
nohup python app.py &
```