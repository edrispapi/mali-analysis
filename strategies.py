from indicators import compute_rsi, compute_macd

def basic_rsi_strategy(prices, buy_threshold=30, sell_threshold=70):
    """استراتژی ساده بر اساس RSI"""
    rsi_series = compute_rsi(prices)
    last_rsi = rsi_series.iloc[-1]
    if last_rsi < buy_threshold:
        return "Buy"
    elif last_rsi > sell_threshold:
        return "Sell"
    else:
        return "Hold"

def macd_crossover_strategy(prices):
    """سیگنال‌دهی بر اساس کراس مکدی"""
    macd_data = compute_macd(prices)
    macd = macd_data['MACD_12_26_9']
    signal = macd_data['MACDs_12_26_9']
    if macd.iloc[-2] < signal.iloc[-2] and macd.iloc[-1] > signal.iloc[-1]:
        return "Buy"
    elif macd.iloc[-2] > signal.iloc[-2] and macd.iloc[-1] < signal.iloc[-1]:
        return "Sell"
    return "Hold"
