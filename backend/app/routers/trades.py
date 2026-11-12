from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from .. import models, database, schemas

router = APIRouter(
    prefix="/trades",
    tags=["trades"]
)


@router.post("/create", response_model=schemas.TradeCreate)
def create_trades(trade: schemas.TradeCreate ,db: Session = Depends(database.get_db)):
    db_trade = models.Trade(**trade.model_dump())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

@router.get("/get", response_model=list[schemas.Trade])
def get_trades(db: Session = Depends(database.get_db), search: Optional[str] = ""):
    return db.query(models.Trade).order_by(models.Trade.trade_date.desc()).filter(models.Trade.trade_type.contains(search)).all()

@router.get("/get/{trade_id}",response_model=schemas.Trade)
def get_trade_id(trade_id: int, db: Session = Depends(database.get_db)):
    trade = db.query(models.Trade).filter(models.Trade.id == trade_id).first()

    if not trade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Trade with id {trade_id} not found")

    return trade