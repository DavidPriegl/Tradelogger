from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import case, func
from sqlalchemy.orm import Session
from . import models, database, schemas


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tradelogger API működik"}

@app.get("/trades", response_model=list[schemas.Trade])
def get_trades(db: Session = Depends(database.get_db)):
    return db.query(models.Trade).order_by(models.Trade.trade_date.desc()).all()

@app.post("/trades", response_model=schemas.TradeCreate)
def create_trades(trade: schemas.TradeCreate ,db: Session = Depends(database.get_db)):
    db_trade = models.Trade(**trade.model_dump())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

@app.get("/trades/{trade_id}",response_model=schemas.Trade)
def get_trade_id(trade_id: int, db: Session = Depends(database.get_db)):
    trade = db.query(models.Trade).filter(models.Trade.id == trade_id).first()

    if not trade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Trade with id {trade_id} not found")

    return trade

@app.get("/portfolio", response_model=list[schemas.Portfolio])
def get_portfolio(db: Session = Depends(database.get_db)):
    portfolio = db.query(models.Trade.symbol,
                          func.sum(
                              case((models.Trade.trade_type == "BUY", models.Trade.quantity), else_=-models.Trade.quantity)
                              ).label("total_quantity")
                              ).group_by(models.Trade.symbol).all()
    
    return portfolio