# 웹 크롤링
- web(거미줄) + crawling(기어다니다)
- 웹에서 정보를 얻는 기술 

<br>

### CSS 고급
- 형제 선택자
  - 동일한 부모를 가진 요소들 중에 특정 요소를 선택하는데 사용 
  - 인접 형제 선택자 (A + B)
  - 일반 형제 선택자 (A ~ B)

- `nth-of-type()` 선택자
  - 특정 유형의 요소 중 특정 순서에 해당하는 요소를 선택할 때 사용
  - div.main > a:nth-of-type(3)
  - div.main > a:nth-of-type(even)
    - 짝수
  - div.main > a:nth-of-type(odd)
    - 홀수
  - div.main > a:nth-of-type(2n+1)
    - 식 1,3,5,7....

- :not(X) 선택자
  - 특정 선택자(x)와 매칭되지 않는 요소를 선택할 때 사용
    - div:not(#fancy)

- 속성 선택자
  - 특정 속성을 기준으로 HTML요소를 선택할 때 사용

<br><br>

### 정적 페이지 크롤링
1. 데이터 받아오기
2. 데이터 뽑아내기  
&nbsp;  - BeautifulSoup4 

객체: 데이터와 명령어를 모두 가질 수 있는 자료형 

<br>

- select_one: 매칭되는 태그중 첫번째 반환
- attrs: 속성(딕셔너리로 표현됨)
- strip(): 앞뒤 공백문자들 제거
- select(): 선택자에 매칭되는 태그 전체를 리스트로 반환 
- find, find_all: 텍스트를 기준으로 찾을 수 있게 도와줌
  - select, select_one은 텍스트 기준으로 찾을 수 **없다**
  - 태그 안에 다른 태그가 있으면 문자열 매칭이 되지 않는다  

<br>

#### 파라미터 종류가 많은 경우
- 구글 개발자 도구에서 파라미터를 복사 
- 파라미터들을 딕셔너리 형태로 만든다음 요청할때 같이 보냄 

#### 상세페이지 크롤링 하는 방법
- for 문 안쪽에서 추가로 요청을 보낼 수 있음
- 목록에서 크롤링한 링크로 상세페이지를 요청 

#### 서버 요청 거절 해결

```
# 오류 코드 
AttributeError: 'NoneType' object has no attribute 'text'
```
- 서버에서 요청 거절을 했기 때문에 html코드를 가져올 수 없었다
- Header를 추가하여 서버를 속이면 해결 
```
header = {
    'User-Agent' : 'Mozilla/5.0',
    'Referer' : 'url 주소'
}
```

#### SSLError
- 인증오류로 인증을 비활성화하면 된다 
- verify=False

<br><br>




