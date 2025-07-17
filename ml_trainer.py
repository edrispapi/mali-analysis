import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_price_predictor(features, targets):
    """مدل پیش‌بینی قیمت با جنگل تصادفی"""
    X_train, X_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return model, score  # مدل آموزش‌دیده و دقت آن
