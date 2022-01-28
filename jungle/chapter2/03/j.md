# 자주 쓰이는 jQuery

## input 박스 값 가져오기

```html
<div class="form-group">
    <label for="exampleInputEmail1">아티클 URL</label>
    <input id="post-url" type="email" class="form-control" aria-describedby="emailHelp"
        placeholder="">
</div>
```

값 가져오기

```javascript
let url = $('#post-url').val();
url // input 박스 안에 적혀있는 내용이 출력된다.
```


input 박스안에 적혀있는 글 변경하기


```javascript
$('#post-url').val("새 글입니다.");
```


## div 숨기기 / 보이기

1. 숨기거나 보이고 싶은 div 태그에 id를 부여합니다.
    
    ```javascript
    <div class="posting-box" id="post-box">
        ...
    </div>
    ```
    
2. 콘솔창에 아래 코드를 입력하여 해당 div가 없어졌다 나타났다 하는 것을 봅니다.
    
    ```javascript
    // id 값이 post-box인 곳을 가리키고, hide()로 안보이게 한다.(=css의 display 값을 none으로 바꾼다)
    $('#post-box').hide();
    
    // show()로 보이게 한다.(=css의 display 값을 block으로 바꾼다)
    $('#post-box').show();
    ```
    
3. div가 없어졌다 나타났다 할 때마다 개발자도구의 Elements 탭에서 해당 div에 적용된 CSS 중에 display 속성이 none과 block 둘 중 하나로 바뀌는 것을 확인할 수 있습니다.



## CSS의 속성 값 가져오기


Elements 탭을 보지 않고도 아래와 같은 방법으로 직접 CSS의 display 속성이 변하는 것을 볼 수 있습니다.

```javascript
$('#post-box').hide();
$('#post-box').css('display');

$('#post-box').show();
$('#post-box').css('display');
```

and

```javascript
$(".wrap").css("width")
$(".card-text").css('color')
// -> 'rgb(33, 37, 41)'
$(".card-title").css('color')
// - > 'rgb(0, 123, 255)'
```

## 태그 내 텍스트 입력하기

- 위에서 본 것처럼 input 박스 안에는 `.val()` 메소드를 이용하여 값을 입력할 수 있습니다.
- 그 외의 경우에는 대부분 시작태그와 종료태그 사이에 있는 텍스트가 화면에 표시되며, 이 값은 아래와 같이 `.text()` 메소드를 이용하여 접근할 수 있습니다.


 1. 원하는 태그에 id를 부여합니다. 여기서는 '포스팅박스 열기' 버튼의 글씨를 바꿔보겠습니다.
        
```javascript
<button id="btn-posting-box" type="button" class="btn btn-primary">포스팅박스 열기</button>
 ```
        
  2. 아래 코드를 이용하여 글씨를 바꿀 수 있습니다.
        
 ```javascript
let btn_text = $('#btn-posting-box').text(); 
btn_text         // '포스팅박스 열기'가 출력된다.
$('#btn-posting-box').text('포스팅박스 닫기');
 ```

 ## 태그 내 html 입력하기

 - 포스팅하면 카드를 추가하는 등, 특정 태그 안에 새로운 html 요소를 동적으로 추가하고 싶을 때는
 `.append()` 메소드를 사용할 수 있습니다.


1. 우손 원하는 태그에 id를 부여한다.

```html
<div id="cards-box" class="card-columns">
    <div class="card"> ... </div>
    <div class="card"> ... </div>
    <div class="card"> ... </div>
    <div class="card"> ... </div>
    <div class="card"> ... </div>
    <div class="card"> ... </div>
</div>
```

2. 태그 뒤에 원하는 값을 추가한다.

```javascript
$('#cards-box').append("추가 텍스트");
```


## 페이지 로딩이 완료되면 실행하기

- 만약 어떤 기능이 페이지가 로딩되자마자 실행되기를 바란다면 ? 아래와같이 써줄 수 있다.

```javascript
<script>

$(document).ready(function(){
	alert('페이지가 로딩되었습니다.')
});

</script>
```