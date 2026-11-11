from fastapi import FastAPI
from .routers import get_trades, get_trade_id, get_portfolio, create_trades # type: ignore




app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tradelogger API is up"}


app.include_router(get_trades.router)
app.include_router(get_trade_id.router)
app.include_router(get_portfolio.router)
app.include_router(create_trades.router)










