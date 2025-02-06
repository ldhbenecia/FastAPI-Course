from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import service, schemas, database

router = APIRouter(
    prefix="/items",  # api endpoint에서 앞에 선언될 부분 지정
    tags=["items"],  # swagger 전용
)


@router.post("/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemResponse, db: Session = Depends(database.get_db)):
    return service.create_item(db=db, item=item)


@router.get("/", response_model=list[schemas.ItemResponse])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return service.get_items(db, skip=skip, limit=limit)


# id로 조회
@router.get("/id/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = service.get_item(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found Item")
    return db_item
