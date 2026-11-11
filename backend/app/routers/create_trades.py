from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter()

@router.post("/trades", response_model=schemas.TradeCreate)
def create_trades(trade: schemas.TradeCreate ,db: Session = Depends(database.get_db)):
    db_trade = models.Trade(**trade.model_dump())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade