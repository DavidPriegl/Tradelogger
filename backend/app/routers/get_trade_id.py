from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter()

@router.get("/trades/{trade_id}",response_model=schemas.Trade)
def get_trade_id(trade_id: int, db: Session = Depends(database.get_db)):
    trade = db.query(models.Trade).filter(models.Trade.id == trade_id).first()

    if not trade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Trade with id {trade_id} not found")

    return trade