from pydantic import BaseModel


# 기본 클래스
class ItemBase(BaseModel):
    name: str


# DB에서 조회된 유저 정보 반환
class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True  # SQLAlchlemy 모델과 호환
