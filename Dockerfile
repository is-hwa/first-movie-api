# 베이스 이미지
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 코드 복사
COPY app/ .

# 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
