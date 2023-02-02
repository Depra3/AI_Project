# 내 방, 어디 ? (version2)
![image](https://user-images.githubusercontent.com/120995529/216347597-1ff2140e-78d4-424d-8ffc-4ff9fdc269f9.png)

## 개요
### 1. 과제
- **서울시공공데이터**에서 **부동산실거래데이터**를 활용해 월세/전세 시세예측

### 2. 상세 설명
- 전세와 월세를 비교할 수 있는 서비스의 필요성 대두
- 현재 금리 인상 및 보증금 미반환 사고등으로 월세 비중 상승
- 월세 가격인상을 예상에 따른 소비자의 합리적인 소비 방향 예측하기

### 3. 팀 구성
- 사용언어 : Python
- 작업툴 : VS code
- 인원 : 7명
- 주여 업무 : Streamlit 라이브러리를 이용한 웹개발 구현 코드 작성
- 기간 : 2023-01-30 - 2023-02-10

### 라이브러리 버전
***
- streamlit : 1.17.0v
    - from streamlit_option_menu import option_menu
- pandas : 1.5.3v
- numpy : 1.24.1v
- matplotlib : 3.6.3v

## 소스코드 설명
***




### 99 . 팀 구성
- 작업 툴 : Python
- 인원 : 7명
  - AI : 3명
  - 웹개발 : 4명
- 주요 업무 : 웹개발 코드 구현
- 기간 : 
## 기간
### 2023-01-30
***
### 2023-02-01
## 개발팀
- 오늘 한 것 : 
  - 홈페이지 기본적인 구상
  - 거래 횟수가 많은 지역 순으로 데이터 정렬
  - sidebar에서 조건에 맞는 검색 기능
  - 보증금, 월세, 면적의 최소, 최댓값을 지정해주는 슬라이더
  - 버튼 누를 시 선택된 값에 해당하는 검색 결과
  - 면적 제곱미터를 평수로 변환하는 람다식
  - 필요한 칼럼을 조인하여 데이터 가공
  - 특정 칼럼에서 특정문자 삭제
  - 게시판 UI 및 기능 구현
  - sqlite 데이터베이스 연동
  - 코드 동기화
***
- 오늘 못한 것 :
  - 인덱스페이지에 정렬한 데이터 추출
  - 전세와 월세를 동시에 보여주는 기능
    - 보증금 월세 범위가 예상보다 컸음
  - 게시글 수정 & 삭제 기능
    - 추후에 HTML 활용하여 추가 예정
***
- 내일 할 것 :
  - 데이터 추가 핸들링
  - 홈페이지 디자인 마무리
  - 전세예측 페이지 구현
  - 게시글 수정 & 삭제 기능
  - 건의사항 내용 칸 늘리기
***
### 2023-02-02
## 개발팀
- 오늘 한 것 :
  - 홈페이지 UI 디자인 변경
  - 홈페이지 DataFrame 구성 변경
  - 월/전세 전체 검색기능
  - 월세, 보증금, 면적 검색할 때 최소, 최대값 입력 받는 기능
  - 건의사항 목록 간격 수정
  - 건의사항 제목, 사용자명 검색 기능

- 오늘 못한 것 :
  - 지역에 맞춘 keyword 알고리즘
  - 건의사랑 게시글 조회, 수정, 삭제 기능

- 내일 할 것 :
  - 홈페이지 keyword 알고리즘 구현
  - 건의사항 검색 UI 수정
  - 건의사항 내용 검색 기능 (디버깅)
  - 건의사항 검색 시 목록 수정
  - 건의사항 목록 간격
  - 월세, 보증금, 면적 select_slider 입력 ==> input 값도 변경
### 팀
***



## 부동산 실거래가를 이용하여 본인 자산 및 연봉을 확인하여 추천 매물 보여주기
- 신용등급하는 API
### 1. 자산 및 신용등급 입력
### 2. 추천매물(필터링)
### 3. 월세 시세 보여주기 (전세, 매매)
### 구현 X
*** 
### 1. 실거래 현황 

### 
***
***
### 설치방법
- MacOS
"""
VS code..~~

streamlit run 파일명(ex:app.py)
"""
- Windows
- Ubuntu
***
## 웹개발 Framewoke : Streamlit
### page1 : 인덱스
### page2 : 월세 검색
### page3 : 전세 예측
### page4 : 건의사항
***
***
### 2023-12-31
***
### 2023-02-01
- 오늘 한 것 : 
  - 홈페이지 기본적인 구상
  - 거래 횟수가 많은 지역 순으로 데이터 정렬
  - sidebar에서 조건에 맞는 검색 기능
  - 보증금, 월세, 면적의 최소, 최댓값을 지정해주는 슬라이더
  - 버튼 누를 시 선택된 값에 해당하는 검색 결과
  - 면적 제곱미터를 평수로 변환하는 람다식
  - 필요한 칼럼을 조인하여 데이터 가공
  - 특정 칼럼에서 특정문자 삭제
  - 게시판 UI 및 기능 구현
  - sqlite 데이터베이스 연동
  - 코드 동기화
***
- 오늘 못한 것 :
  - 인덱스페이지에 정렬한 데이터 추출
  - 전세와 월세를 동시에 보여주는 기능
    - 보증금 월세 범위가 예상보다 컸음
  - 게시글 수정 & 삭제 기능
    - 추후에 HTML 활용하여 추가 예정
***
- 내일 할 것 :
  - 데이터 추가 핸들링
  - 홈페이지 디자인 마무리
  - 전세예측 페이지 구현
  - 게시글 수정 & 삭제 기능
  - 건의사항 내용 칸 늘리기
