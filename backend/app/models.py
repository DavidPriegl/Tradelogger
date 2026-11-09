from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from .database import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), nullable=False)
    trade_type = Column(String(4), nullable=False)
    quantity = Column(Numeric(10, 4), nullable=False)
    price_per_unit = Column(Numeric(12, 2), nullable=False)
    trade_date = Column(DateTime, server_default=func.now())