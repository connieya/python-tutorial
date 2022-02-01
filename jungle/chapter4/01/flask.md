# flask 란 ?

파이썬으로 쓰인 웹 프레임워크로, 서버를 구동하는 데 필요한 여러 기능들을 제공한다.

# flask 기초 : 서버 실행

- `python3 -m venv .venv`로 가상 환경을 만들고 `.venv/scripts/activate`로 가상 환경을 활성화시킨다. Interpreter도 가상환경의 것으로 바꾼다.
- project interpreter에서 flask 패키지를 설치한다.
- app.py라는 새 파일을 만든 후 아래 코드를 붙여넣는다.

## flask 시작 코드

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
```

# flask 기본 폴더 구조

static , templates , app.py


# flask : html 파일 내 이미지를 불러오기

일반 HTML에서 이 파일을 불러온다면 img의 src를 이런 식으로 쓸 것입니다. rome.jpg의 경우 index.html이 있는 templates 폴더의 상위 폴더(코드로는 ..라고 씁니다) 안의 static 폴더 안에 있기 때문입니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
			integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
		  crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <h1>서버를 만들었다!</h1>
    <img src="../static/rome.jpg"/>
</body>
</html>
```

하지만 flask에서 띄울 때는 flask에서 미리 정의된 방법으로 경로를 입력해주어야 합니다. 그래서 ststic 폴더 안의 rome.jpg의 경로는 아래와 같이 써줍니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
			integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
		  crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <h1>서버를 만들었다!</h1>
    <img src="{{ url_for('static', filename='rome.jpg') }}"/>
</body>
</html>
```

# API 만들기

## GET 요청 API 코드

```python
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
```

## GET 요청 확인 Ajax 코드

```javascript
$.ajax({
    type: "GET",
    url: "/test?title_give=봄날은간다",
    data: {},
    success: function(response){
       console.log(response)
    }
  })
```

## POST 요청 API코드

```python
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
```
## POST 요청 확인 Ajax코드

```javascript
$.ajax({
    type: "POST",
    url: "/test",
    data: { title_give:'봄날은간다' },
    success: function(response){
       console.log(response)
    }
  })
```