from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter()

@router.get("/trades", response_model=list[schemas.Trade])
def get_trades(db: Session = Depends(database.get_db)):
    return db.query(models.Trade).order_by(models.Trade.trade_date.desc()).all()