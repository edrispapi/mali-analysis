from celery import Celery
from market_fetcher import MarketFetcher
from db_manager import get_db
from market_models import PriceData

celery_app = Celery('market_tasks', broker='redis://localhost:6379/0')

fetcher = MarketFetcher(base_url="https://api.example.com", api_key="MY_KEY")

@celery_app.task
def scheduled_price_update():
    """دریافت خودکار داده بازار و ذخیره آن"""
    db = next(get_db())
    prices = fetcher.fetch_quotes()
    for symbol, price in prices.items():
        new_record = PriceData(symbol=symbol, price=price)
        db.add(new_record)
    db.commit()
    db.close()
