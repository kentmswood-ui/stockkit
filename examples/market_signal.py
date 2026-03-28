"""
StockKit API Example: Market Sentiment Signal
https://stockkit.net
"""
import requests
import json

def get_market_signal() -> dict:
    """Get overall market mood/sentiment."""
    r = requests.get("https://stockkit.net/api/signal")
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    signal = get_market_signal()
    print(json.dumps(signal, indent=2, ensure_ascii=False))
