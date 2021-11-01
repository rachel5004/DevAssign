# StoveDevAssign
Stove DevCamp Assignment Topic 1: URL Shortener

## 🛠 Environment
- Python 3.9.2
- Flask 2.0.2
- Werkzeug 2.0.2


## 🎊 Quick Start
```shell
# clone project repo
git clone https://github.com/rachel5004/StoveDevAssign.git
cd <project>

# install libs
pip install -r requirements.txt

# DB setting
flask db init
flask db migrate
flask db upgrade

# start app
export FLASK_APP=urlcutter/__init__.py; export FLASK_ENV=development; flask run
```

## 🎯 요구사항

- [ ] 1. 웹 페이지 입력폼에 URL 입력 시 단축된 결과 출력
- [ ] 2. 브라우저의 주소창에 단축 URL 입력 시 기존 URL로 리다이렉트
- [ ] 3. 같은 URL 입력 시 동일한 결과값 도출
- [ ] 4. 결과값은 주소를 제외하고 8글자 이내로 생성


<br/>

## 📝 API
### 단축url 생성 (Query String)

| method | uri |
|---|---|
|GET|/url|
|POST|/url|

```javascript
{
 // post의 경우
 request: {
   url : ""
 }
 response: "shortcut"
}
```

### 단축url로 이동

| method | uri |
|---|---|
|GET|/\<shortcut>|

```javascript
{
 response: CODE 302
}
```

<br/>

## ❓ About shortcut generater
### Base62 vs. Base64
base64를 사용하면 더 짧은 길이로 축소가능하지만, base64는 '+', '=', '/'와 같은 문자들이 포함되어 URL SAFE하지가 않습니다.
때문에 base62로 인코딩했습니다.

### 원본URL vs. id
원본 url을 그대로 인코딩하면 결과값이 길어지게 되므로, DB에 저장 후 생성된 id값을 기반으로 단축URL을 생성했습니다.
