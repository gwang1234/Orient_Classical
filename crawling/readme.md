# 웹 크롤링
- web(거미줄) + crawling(기어다니다)
- 웹에서 정보를 얻는 기술 

<br>

## CSS 고급
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

## 파이썬 문법
- str.maketrans: 문자열 변환을 위한 `매핑 테이블`을 생성
- translate: 매핑된 테이블에 따라 문자열이 변환 

<br><br><br><br>

## 정적 페이지 크롤링
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

<br><br><br><br>

## 셀레니움
- driver.get - 원하는 페이지로 이동 
- driver.back - 뒤로가기
- driver.forward - 앞으로가기
- driver.refresh - 드라이버 새로고침
- driver.current_url - 현재 url 확인 
- driver.title - 페이지 제목 확인
- driver.close - 현재 창 닫기
- driver.quit - 모든 창을 닫고, 웹트라이버 세션 종료
- `driver.find_element` - 웹페이지에서 첫번째로 일치하는 태그를 찾아 반환해줌 
  - 일치하는 태그가 없다면 `NoSuchElementException` 반환

#### NoSuchWindowException
- 드라이버가 브라우저 창을 참조하지 못할때 발생하는 오류
- 창이 열려있는지 확인하기 

#### 동적 대기 기법 
- 웹페이지의 태그가 즉시 로드되지 않고, 어떤 동작이나 시간이 지난 후에 나타나는 경우가 있다
- 이러한 동적 태그를 처리하기 위해 셀레니움에서 `동적 대기 기법` 제공
- 암시적 대기 - 태크 찾기 위해 동작하는 최대 시간 설정 
- 명시적 대기 - 조건이 만족할 때까지 대기 

#### 고급 입력 컨트롤
- clear - 입력창의 모든 텍스트 삭제
- `순차적 키 입력` - 키보드의 특정 키들을 미리 정한 순서대로 자동으로 입력하는 것

<br>

오류
```
search.send_keys('코딩')
search.send_keys(Keys.CONTROL, 'a')
search.send_keys(Keys.CONTROL, 'c')

결과: 코딩search.send_keys(Keys.CONTROL, 'a')
```
- 오류 원인
   - 연속적인 호출로 인해 키 입력이 누적적으로 추가되면서 예상하지 못한 결과가 발생
- 해결
  - time.sleep

#### 셀렉트박스 조작
- 셀레니움에서 제공하는 select 클래스 이용

#### 여러 페이지 관리
- 페이지 안에 다른 페이지가 있는 경우, 다른 페이지를 제어할 수 없다
  - **웹 드라이버는 한번에 하나의 페이지만 제어할 수 있기 때문**
- 이럴 경우, 서브 페이지를 바라볼 수 있도록 드라이버를 전환 

<br><br><br><br>

## 동적 페이지 크롤링


정적 페이지와 동적 페이지 구분
- f12 -> 톱니바퀴 -> disavble javascript 체크 -> 화면 새로고침 후 확인 