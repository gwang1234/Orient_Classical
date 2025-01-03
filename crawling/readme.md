# 웹 크롤링
- web(거미줄) + crawling(기어다니다)
- 웹에서 정보를 얻는 기술 

<br>

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

<br><br>

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
  


