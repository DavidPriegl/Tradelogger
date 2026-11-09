from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, schemas
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tradelogger API működik"}

@app.get("/trades", response_model=list[schemas.Trade])
def get_trades(db: Session = Depends(database.get_db)):
    return db.query(models.Trade).order_by(models.Trade.trade_date.desc()).all()

