# KIM & JEONG

---
🔔 본 프로젝트는 삼성 청년 SW 아카데미 9기 1학기 관통 프로젝트 결과물입니다.

<br><br>

## 개요

---

- 금융 상품 관련 다양한 서비스 제공을 목적으로 예적금 금융상품들의 금리 비교 및 회원에 따라 금융 상품 추천 기능을 제공
- 부가적인 정보 서비스 제공으로 해당 날짜 기반 환율 계산 서비스 및 원하는 은행 검색 서비스 제공

<br><br>

## 프로젝트 기간

---

- 2023년 5월 16일 ~ 2023년 5월 26일

<br><br>

## 팀원 및 업무 분담

---

<table>
  <thead>
    <tr>
      <th>이름</th>
      <th>역할</th>
      <th>구현 기능</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>김주현</td>
      <td>팀장</td>
      <td>Front-End (메인 페이지 디자인, 게시판 검색기능, 환율 계산, 은행 지도 검색 기능, 금융 상품 비교 기능 등)</td>
    </tr>
    <tr>
      <td>정도현</td>
      <td>팀원</td>
      <td>Back-End (Rest API 설계, Django/Vue 디버깅, DB 테이블 수정, 금융 상품 추천 알고리즘 설계, Back-Front 간 데이터 전송 등)
</td>
    </tr>
  </tbody>
</table>

<br><br>

## 주요 기능

---

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Depth1</th>
      <th>Depth2</th>
      <th>내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P01-1</td>
      <td>로그인 / 회원 관리</td>
      <td>회원 가입</td>
      <td>
        - 아이디, 비밀번호, 닉네임, 나이, 성별, 소득 입력<br>
        - 아이디 입력 시 중복 여부 확인<br>
        - 비밀번호 확인을 통해 일치 여부 확인<br>
        - 회원 가입 시 자동으로 로그인<br>
        - 회원 가입 시 부정확한 데이터(나이가 음수, 제 3의 성별) 입력 방지
      </td>
    </tr>
    <tr>
      <td>P01-2</td>
      <td>로그인 / 회원 관리</td>
      <td>로그인</td>
      <td>
        - 아이디, 비밀번호를 통해 로그인<br>
        - 회원 목록에 없는 아이디로 로그인 시 오류 메시지 출력<br>
        - 아이디, 비밀번호 불일치 시 오류 메시지 출력<br>
        - 아이디, 비밀번호가 공란으로 로그인시 오류 메시지 출력<br>
        - 로그인 시 메인 페이지로 이동, 로그아웃 시 로그인 페이지로 이동
      </td>
    </tr>
    <tr>
      <td>P02-1</td>
      <td>프로필</td>
      <td>금융 상품 확인</td>
      <td>
        - 회원가입 시 입력한 자신의 연령, 소득을 기준으로 금융 상품 추천 서비스 제공<br>
        - 유저가 가입한 금융 상품 목록 제공<br>
        - 가입한 상품, 추천받은 상품의 상세 정보를 확인 가능<br>
        - 가입한 상품의 이자율을 차트로 확인 가능<br>
      </td>
    </tr>
    <tr>
      <td>P02-2</td>
      <td>프로필</td>
      <td>회원 정보 수정</td>
      <td>
        - 프로필 페이지에서 회원 정보 수정 페이지로 이동 가능<br>
        - 닉네임 변경 가능<br>
        - 금융 상품 추천 서비스에 관련된 현재 소득 변경 가능<br>
        - 회원 정보 수정 시 프로필 페이지로 이동<br>
      </td>
    </tr>
    <tr>
      <td>P03-1</td>
      <td>부가 서비스</td>
      <td>금융 상품 공시</td>
      <td>
        - 금융감독원 금융상품통합비교공시 API 사용<br>
        - 예금 정보, 적금 정보 버튼을 통해 원하는 범주의 상품 조회 가능<br>
        - 체크박스를 통해 세부사항 검색 가능(저축기간, 가입방법, 은행)<br>
        - 상품명, 은행명, 가입 방법, 저축기간 별 이자율 정보 제공<br>
        - 상품명 클릭시 해당 상품의 자세한 정보를 조회<br>
        - 은행명 클릭시 해당 은행의 위치를 검색할 수 있는 지도 검색 페이지로 이동<br>
      </td>
    </tr>
    <tr>
      <td>P03-2</td>
      <td>부가 서비스</td>
      <td>환율 정보 확인</td>
      <td>
        - 한국수출입은행 환율정보 API 사용<br>
        - 각 국가의 화폐단위-원 간의 환율 리스트 제공<br>
        - 비교 기준 화폐와 비교 대상 화폐를 선택하여 두 화폐 간의 환율 비교 가능<br>
        - 루피아, 옌 등 환율 단위가 다른 화폐는 Backend에서 평준화 처리<br>
      </td>
    </tr>
    <tr>
      <td>P03-3</td>
      <td>부가 서비스</td>
      <td>은행 위치 검색</td>
      <td>
        - 카카오맵 API 사용<br>
        - 전국의 시/도 와 시/군/구 선택 가능<br>
        - 금융상품이 등록된 모든 은행 선택 가능<br>
        - 금융상품 상세 조회 페이지에서 선택한 은행 자동 검색<br>
        - 인포윈도우를 선택시 해당 은행의 정보 상세 조회<br>
      </td>
    </tr>
    <tr>
      <td>P04-1</td>
      <td>게시판</td>
      <td>공지 게시판</td>
      <td>
        - 관리자 권한을 가진 사용자만 글 작성, 수정, 삭제 가능<br>
        - 댓글 사용이 불가능한 게시판<br>
      </td>
    </tr>
    <tr>
      <td>P04-2</td>
      <td>게시판</td>
      <td>뉴스 게시판</td>
      <td>
        - 관리자 권한을 가진 사용자만 글 작성, 수정, 삭제 가능<br>
        - 일반 사용자는 로그인 후 작성된 게시물에 댓글 작성 가능<br>
      </td>
    </tr>
    <tr>
      <td>P04-3</td>
      <td>게시판</td>
      <td>유저 게시판</td>
      <td>
        - 카테고리를 설정하여 글 작성 가능<br>
        - 로그인 된 사용자만 글 작성 및 수정 가능<br>
        - 로그인 된 사용자만 댓글 작성 가능<br>
        - 작성자가 아닌 일반 사용자는 글 / 댓글 삭제 및 수정 불가<br>
        - 관리자 권한이 있는 사용자는 모든 글 / 댓글 삭제 수정 가능
      </td>
    </tr>
  </tbody>
</table>

<br><br>

## 서비스 기능 설명

---

### ✨ 메인 페이지 : Home
- 최상단에는 모든 페이지에 존재하는 nav 바를 만들었다. 아이콘의 경우 기능에 맞게 그림판으로 직접 만들었고 주요 기능 서비스로 이동할 수 있도록 설정해두었다. 메인 페이지는 캐서셀로 금융 상품 서비스, 환율 계산 서비스, 지도 검색 서비스를 간단히 소개하는 문구와 바로 페이지를 이동할 수 있는 버튼을 구현하였다. 또한 커뮤니티 게시판들의 최신 글의 제목을 간단하게 띄우고 해당 게시판으로 바로 이동할 수 있는 버튼을 구현하였다. 

<br>

### ✨ 메인 페이지 : 환율 계산 서비스 (API)
- 원과 다른 화폐 뿐만 아니라 외국의 화폐끼리도 환율 계산이 가능하도록 구현했다. API에는 원 환율만 나오기 때문에 이 값을 가지고 적절한 수식처리를 해서 외국의 화폐끼리도 환율 비교를 할 수 있도록 했다. 또한 사용자가 한 눈에 모든 국가의 화폐를 볼 수 있도록 국가, 화폐 단위, 원 기준 환율을 리스트로 출력해서 보여주도록 구현했다. 

<br>

### ✨ 메인 페이지 : 은행 검색 서비스 (KAKAO MAP API)
- 지역과 은행을 선택하면 해당 지역에 있는 모든 은행이 검색되도록 했다. 지역의 경우 시/도와 시/군/구 데이터를 vuex에 직접 작성하였다. 또한 모든 페이지에서 금융 상품을 상세조회 했을 때 은행명을 클릭하면 해당 은행을 지도에서 자동으로 검색하도록 했다. 

<br>

### ✨ 메인 페이지 : 게시판

- 게시판은 일반 유저들을 대상으로 한 유저게시판과 금융 상품 관련 뉴스가 게제되는 뉴스 게시판, 그리고 사이트 주요 공지사항을
전달하는 공지게시판으로 구성했다.

<br>

### ✨ 메인 페이지 : 회원별 맞춤 금융 상품 추천 알고리즘

- 회원별 추천 알고리즘은 장고 ORM을 이용해 원하는 데이터를 선별 후 가공하는 방식을 사용했다.
  1. 회원들이 가입한 예적금 상품을 저장한 필드를 serializer를 이용해 따로 선별했다.
  2. accounts의 views.py에서 DB에 있는 유저들이 가입한 예적금 상품을 호출한 뒤, 각 상품 가입자의 평균 나이와 평균 소득을 산출했다.
  3. 현재 로그인 된 유저의 나이 / 소득과 비교하여 절대값 차이가 가장 작은 모델 순서대로 추천 상품을 구성했다.

<br><br>

## 서비스 구현 Review
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Depth1</th>
      <th>Depth2</th>
      <th>내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P01-1</td>
      <td>로그인 / 회원 관리</td>
      <td>회원 가입</td>
      <td>
        회원 탈퇴 기능을 vue애서 가능하게 만들지 못한 것을 뒤는게 알아차려서 안타까웠다. 이후의 프로젝트에서는 기획 단계에서 내가 해야할 부분을 명확히 짚어야 할 필요성을 느꼈다. 
      </td>
    </tr>
    <tr>
      <td>P01-2</td>
      <td>로그인 / 회원 관리</td>
      <td>로그인</td>
      <td>
        이번 프로젝트에서는 로그인 방식으로 로컬스토리지 기반의 토큰 인증을 이용했다. 다른 방식을 시도하지 못했던 점이 아쉽기에 프로젝트 이후 JWT나 세션 방식 로그인에 대해 공부해보고 싶다.
      </td>
    </tr>
    <tr>
      <td>P02-1</td>
      <td>프로필</td>
      <td>금융 상품 확인</td>
      <td>
        이전에 진행한 프로젝트를 많이 참고했던 파트이다. 원하는 성과는 냈지만, sql문이 아닌 orm위주로 코드를 구성하면서 sql에 대한 추가적인 학습 필요성을 느끼게 되었다.
      </td>
    </tr>
    <tr>
      <td>P02-2</td>
      <td>프로필</td>
      <td>회원 정보 수정</td>
      <td>
        회원 가입 편의를 위해 필드에서 email을 제외한 것으로 회원 정보 수정 기능 면에서 구현하지 못한 부분이 많이 발생했다. 경험해보지 못한 제 3자 rest API로 프로젝트를 진행하는 일이 다시 생길 때는 이런 일이 없도록 구현하려고 한다.
      </td>
    </tr>
    <tr>
      <td>P03-1</td>
      <td>부가 서비스</td>
      <td>금융 상품 공시</td>
      <td>
        - Django에서 API를 통해 데이터를 받아오는 url을 생성한 뒤 Vue에서 해당 url을 통해 Vuex의 state에 저장하고 vue에서 이 데이터를 가공하여 사용자에게 출력해주는 구조로 구현했다. 
      </td>
    </tr>
    <tr>
      <td>P03-2</td>
      <td>부가 서비스</td>
      <td>환율 정보 확인</td>
      <td>
      Django에서 API를 통해 데이터를 받은 뒤, vue에서 필요한 형태로 전처리하는 작업을 거쳤다. 환율 단위가 다른 화폐는 수식을 통해 다른 화폐들과 단위를 맞춰주었고 국가, 화폐단위, 환율 필드만 선택해서 vue로 넘겨주었다. vue에서 비교하려는 두 화폐의 환율은 모두 원 단위였기 때문에 비교 시 각 화폐 단위를 기준으로 출력할 수 있도록 적절한 수식 처리를 하였다. 
      </td>
    </tr>
    <tr>
      <td>P03-3</td>
      <td>부가 서비스</td>
      <td>은행 위치 검색</td>
      <td>
      카카오맵 API를 통해 데이터를 vue에서 직접 받아서 구현했다. 지역 데이터의 경우 vuex에 하드코딩으로 작성했다. 금융 상품 상세 정보 조회 페이지에서 은행명을 클릭하면 해당 은행을 검색어로 지도 페이지에서 자동 검색하게 만들었다. 
      </td>
    </tr>
    <tr>
      <td>P04-1</td>
      <td>게시판</td>
      <td>공지 게시판</td>
        관리자만 게시글을 작성할 수 있고 댓글 기능은 없는 게시판이다. 글 작성 버튼의 경우 일반유저는 화면에 보이지 않게 했다. 
      <td>
    </tr>
    <tr>
      <td>P04-2</td>
      <td>게시판</td>
      <td>뉴스 게시판</td>
      <td>
        관리자만 게시글을 작성할 수 있고 댓글 기능도 존재하는 게시판이다. 글 작성 버튼의 경우 일반유저는 화면에 보이지 않게 했다. 
      </td>
    </tr>
    <tr>
      <td>P04-3</td>
      <td>게시판</td>
      <td>유저 게시판</td>
      <td>
        모든 유저가 게시글과 댓글을 작성할 수 있는 게시판이다. 카테고리 별로 게시글을 분류했고 게시글을 작성할 때 정해진 카테고리 내에서 선택할 수 있게 하였다. 
      </td>
    </tr>
  </tbody>
</table>

### Frontend

-Vue

---

### 😖 프로젝트 구현 과정에서 기술적인 아쉬움
#### 김주현
- 프로젝트 초반, 페이지를 새로고침을 하면 vuex의 state에서 데이터를 가져오기 전에 페이지 렌더링이 끝나서 데이터를 화면에 출력하지 못하는 문제가 있었는데 팀원의 도움을 받아 vuex getters에 데이터를 저장한 뒤 vue에서 사용하는 방식으로 해결하였다. 수업시간에 배운 모든 기능을 적절히 활용하지 못한 점이 아쉬웠다. 
- 웹페이지를 반응형으로 구현해서 화면 크기에 따라 사용자에게 다르게 보이도록 하고 싶었지만 시간이 너무 빠듯하여 이를 실행하지 못했다. 프로젝트 기간이 짧은 것도 있지만 개인적으로 html과 css 숙련도가 아쉽다는 생각이 들었다. 



#### 정도현
- 온라인에 공개된 코드나 Chat-GPT가 추천을 하는 코드가 주로 vue3로 이루어져 있었다.
- ssafy 과정에서는 vue2로 진행했기에 일부 코드가 작동이 되지 않는 오류가 있었고, ssafy 교육에서 vue3를 다루지 않았던 점이 아쉬웠다.
- 프로젝트 직전은 vue와 javascript 기반 수업이었다. 때문에 python 관련 지식을 떠올리고 활용하는 데 어려움을 겪었다.
- 장고에서 form과 serializer의 유용성을 직접 체험할 수 있었다.
- 프로젝트 마무리를 지으면서 뉴스 게시판에 동영상이나 이미지를 올리지 못하는 부분을 깨달았다. 좀 더 구체적인 기획의 필요성을 느꼈다.
- 로그인하지 않은 유저가 글이나 댓글을 작성하는 방식을 어떻게 구현할지 궁금함이 생겼다. 이를 추후 학습으로 보완하고자 한다.

<br>

### 😖 추후 프로젝트 시 고려해야 할 사항

- 첫 프로그래밍 관련 프로젝트다 보니 프로젝트 기획 단계에서 미숙했던 부분들이 아쉽다.
- 프로젝트를 진행하면서 초반부에 모델이나 프로그램 컨셉에 대해 보다 명확하게 정하고 코딩을 시작해야 함을 깨달았다.