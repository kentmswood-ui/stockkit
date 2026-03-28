"""
StockKit API Example: Get Real-time Stock Quote
https://stockkit.net
"""
import requests

def get_quote(symbol: str, market: str = "US") -> dict:
    """Fetch real-time quote from StockKit API."""
    r = requests.get(f"https://stockkit.net/api/quote", params={"symbol": symbol, "market": market})
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    # US Stock
    quote = get_quote("NVDA", "US")
    print(f"NVDA: ${quote.get('price', 'N/A')} ({quote.get('changePct', 'N/A')}%)")

    # China A-Share
    quote = get_quote("600519", "CN")
    print(f"600519: ¥{quote.get('price', 'N/A')}")

    # Hong Kong
    quote = get_quote("0700", "HK")
    print(f"0700.HK: HK${quote.get('price', 'N/A')}")
