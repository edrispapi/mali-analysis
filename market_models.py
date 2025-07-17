from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PriceData(Base):
    __tablename__ = "price_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(12), index=True, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

class HistoricalCandle(Base):
    __tablename__ = "historical_candles"
    id = Column(Integer, primary_key=True)
    symbol = Column(String(12), nullable=False)
    open = Column(Float)
    close = Column(Float)
    low = Column(Float)
    high = Column(Float)
    volume = Column(Float)
    time_start = Column(DateTime)
    time_end = Column(DateTime)
