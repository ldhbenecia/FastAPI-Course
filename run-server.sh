#!/bin/bash

# 가상환경 활성화
source ./venv/bin/activate

# 환경 변수 로드 (주석 라인 제외)
export $(grep -v '^#' .env | xargs)

# FastAPI 서버 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
