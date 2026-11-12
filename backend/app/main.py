from fastapi import FastAPI
from .routers import portfolio, trades # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tradelogger API is up"}


app.include_router(trades.router)
app.include_router(portfolio.router)











