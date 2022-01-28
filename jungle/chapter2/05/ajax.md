# Ajax 시작하기

## Ajax 기본 골격

```javascript
$.ajax({
  type: "GET",
  url: "여기에URL을입력",
  data: {},
  success: function(response){
    console.log(response)
  }
})
```

미세먼지 API
```javascript
$.ajax({
  type: "GET", // GET 방식으로 요청한다.
  url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
  data: {}, // 요청하면서 함께 줄 데이터 (GET 요청시엔 비워두세요)
  success: function(response){ // 서버에서 준 결과를 response라는 변수에 담음
    console.log(response) // 서버에서 준 결과를 이용해서 나머지 코드를 작성
  }
})
```

모든 구의 미세먼지 값 찍어보기

```javascript

$.ajax({
  type: "GET",
  url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
  data: {},
  success: function (response) {
    let mise_list = response["RealtimeCityAir"]["row"];
    for (let i = 0; i < mise_list.length; i++) {
      let mise = mise_list[i];
      let gu_name = mise["MSRSTE_NM"];
      let gu_mise = mise["IDEX_MVL"];
      console.log(gu_name, gu_mise);
    }
  },
});
```