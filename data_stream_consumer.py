import json
from kafka import KafkaConsumer
from market_models import PriceData
from db_manager import get_db

def run_consumer(topic="forex_realtime"):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    db = next(get_db())
    for message in consumer:
        data = message.value
        new_price = PriceData(
            symbol=data["symbol"],
            price=data["price"]
        )
        db.add(new_price)
        db.commit()
