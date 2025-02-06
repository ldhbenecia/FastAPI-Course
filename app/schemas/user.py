from pydantic import BaseModel


# 기본 클래스
class UserBase(BaseModel):
    name: str
    email: str


# 유저를 생성할 때 UserBase를 상속 받아 name, email, password 3가지로 생성
class UserCreate(UserBase):
    password: str


# DB에서 조회된 유저 정보 반환
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # SQLAlchlemy 모델과 호환
