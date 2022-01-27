# 배경

## background-color 

background-color 속성은 해당 HTML 요소의 배경색(background color)을 설정합니다.

```html
<style>

    body { background-color: lightblue; }

    h1 { background-color: rgb(255,128,0); }

    p { background-color: #FFFFCC; }

</style>

```

## background-image 

background-image 속성은 해당 HTML 요소의 배경으로 나타날 배경 이미지(image)를 설정합니다.

설정된 배경 이미지는 기본 설정으로 HTML 요소 전체에 걸쳐 반복되어 나타납니다.

```html
<style>

    body { background-image: url("/examples/images/img_background_good.png"); 
    }

</style>
```

## background-repeat 속성
배경 이미지는 기본 설정으로 수평과 수직 방향으로 모두 반복되어 나타납니다.

background-repeat 속성을 이용하면 이러한 배경 이미지를 수평이나 수직 방향으로만 반복되도록 설정할 수 있습니다.

 

다음 예제는 배경 이미지의 수평 반복을 보여줍니다.

```html
<style>

    body { 
        background-image: url("/examples/images/img_man.png"); background-repeat: repeat-x; 
    }

</style>
```

다음 예제는 배경 이미지의 수직 반복을 보여줍니다.

```html
<style>

    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-y; }

</style>
```

배경 이미지가 반복되지 않고 한 번만 나타나게 할 수도 있습니다.

```html
<style>

    body { background-image: url("/examples/images/img_man.png"); background-repeat: no-repeat; }

</style>
```