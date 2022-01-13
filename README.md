#⚽모두의싸커⚽


전 세계에서 가장 인기있는 스포츠 1위 축구!! 당신이 좋아하는 유럽 축구팀들을 응원해 주세요.
좋아요를 누르고 축구팀과 경기에 대해 자유롭게 의견도 남겨보세요. 최정상 리그들의 실시간 순위도 확인할 수 있습니다
**   

<br>

## 1. 제작 기간 & 팀원 소개
- 2022년 1월 10일 ~ 2022년 1월 13일
- 4인 1조 팀 프로젝트
  + 이도경 : 전체페이지 CSS
  + 이상봉 : 메인페이지 CRUD
  + 이제원 : 네이버 해외축구 CRU
  + 황성원 : 로그인 + 회원가입 + MAIN SUB
  
<br>

## 2. 사용 기술
`Back-end`
- Python 3
- Flask 2.0.1
- MongoDB 4.4

`Front-end`
- JQuery 3.5.1
- Jquery
- css

`deploy`
- AWS EC2 (Ubuntu 18.04 LTS)

<br>

## 3. 와이어프레임
![image](https://user-images.githubusercontent.com/97431034/149271020-109cdec6-04bb-4128-ac20-9115b7e686e0.png)
![image](https://user-images.githubusercontent.com/97431034/149271067-21357e7f-bd1c-4b1e-9bd0-870406005b3a.png)
![image](https://user-images.githubusercontent.com/97431034/149271079-a14bf111-f1b2-45ca-9a43-636cba6ea767.png)


## 4. 실행화면 


<br>

## 4. 핵심기능

+ **로그인, 회원가입**   
  :  아이디 유효성 확인 될 시, 데이터 날라가지 않도록 잠금기능 구현
  <br>
  :  회원가입 시, 마우스말고 엔터키로 넘어가는 기능 구현
     enterkey 추가
  


+ **메인페이지 CRUD**   
  : 팀리스트 검색 기능 4가지 버전 <br>
  -각각의 탭 버튼을 클릭 시 해당하는 리그값을 showTeams()함수로 문자열로 받아서 ajax 통신<br>
  -서버에서 showTeam에서 전달받은 리그의 팀 리스트만 find해서 출력
  
  :리뷰박스 기능 구현
  - 유저분들이 좋아하는 팀리스트 들어가 리뷰를 작성 할 수 있는 기능 
  - 유저분들의 아이디 마스킹 처리 진행 
  
  : 순위표 고정 기능 구현
  - 유저분들이 스크롤 하여도, 순위표를 보실 수 있도록 css에 osition: fixed 추가

  
  
<br>

## 5. 개인 회고
