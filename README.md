# 공연예술통합전산망 Open API 파싱
> [공연예술통합전산망](https://www.kopis.or.kr/por/cs/openapi/openApiInfo.do?menuId=MNU_00074&searchType=total&searchWord=) <br>
> [TICKETPARIS 프로젝트](https://github.com/prgrms-be-devcourse/BE-04-TICKETPARIS)

### 목적
- TICKETPARIS 프로젝트에 더미 데이터로 사용될 공연 데이터 파싱
- 파싱한 데이터를 2차 가공하여 DB에 삽입

### 사용 모듈
> pip install로 설치 가능
- requests - 2.31.0
- beautifulsoup4 - 4.12.2
- PyMySQL - 1.1.0

### 실행 방법
1. git clone
2. 3306 포트로 MySQL 구동 
3. DB 스키마 정의 
4. .env 파일 만들고 환경변수 작성 
    ```text
   API_KEY={API_KEY}
    MYSQL_ROOT_PASSWORD={MYSQL root 사용자 계정 비밀번호}
    DATABASE_NAME={DB 스키마 이름}
    ```
5. 가상환경 생성 및 라이브러리 설치
    ```bash
   # 가상환경 생성
    $ python -m venv venv
   
   # 라이브러리 설치
   $ pip install -r requirements.txt
    ```
6. main.py 실행
