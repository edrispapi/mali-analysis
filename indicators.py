import pandas as pd
import pandas_ta as ta

def compute_rsi(prices, period=14):
    """محاسبه اندیکاتور RSI"""
    df = pd.DataFrame(prices, columns=["close"])
    df['rsi'] = ta.rsi(df['close'], length=period)
    return df['rsi']

def compute_macd(prices, fast=12, slow=26, signal=9):
    """محاسبه اندیکاتور MACD"""
    df = pd.DataFrame(prices, columns=["close"])
    macd = ta.macd(df['close'], fast=fast, slow=slow, signal=signal)
    df = pd.concat([df, macd], axis=1)
    return df[['MACD_12_26_9', 'MACDh_12_26_9', 'MACDs_12_26_9']]
