from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import service, schemas, database

router = APIRouter(
    prefix="/users",  # api endpoint에서 앞에 선언될 부분 지정
    tags=["users"],  # swagger 전용
)


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return service.create_user(db=db, user=user)


# 10명의 사용자 조회
@router.get("/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return service.get_users(db, skip=skip, limit=limit)


# id로 조회
@router.get("/id/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = service.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Not found User")
    return db_user
