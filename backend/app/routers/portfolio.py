from fastapi import Depends, APIRouter
from sqlalchemy import case, func
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter()

@router.get("/portfolio", response_model=list[schemas.Portfolio])
def get_portfolio(db: Session = Depends(database.get_db)):
    portfolio = db.query(models.Trade.symbol,
                          func.sum(
                              case((models.Trade.trade_type == "BUY", models.Trade.quantity), else_=-models.Trade.quantity)
                              ).label("total_quantity")
                              ).group_by(models.Trade.symbol).all()
    
    return portfolio