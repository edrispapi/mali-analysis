import numpy as np

def detect_anomalies(prices, window=30, threshold=3.0):
    """یافتن نقاط آنومالی در داده‌های قیمت"""
    prices = np.array(prices)
    rolling_mean = np.convolve(prices, np.ones(window)/window, mode='valid')
    residuals = prices[window-1:] - rolling_mean
    std = np.std(residuals)
    anomalies = np.where(abs(residuals) > threshold * std)[0] + window - 1
    return anomalies.tolist()
