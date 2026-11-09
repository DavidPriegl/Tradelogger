from pydantic import BaseModel, ConfigDict
from typing import Literal
from datetime import datetime

class TradeBase(BaseModel):
    symbol: str
    trade_type: Literal["BUY", "SELL"]
    quantity: float
    price_per_unit: float

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id:int
    trade_date: datetime

    model_config = ConfigDict(from_attributes=True)

class Portfolio(BaseModel):
    symbol: str
    total_quantity: float

    model_config = ConfigDict(from_attributes=True)