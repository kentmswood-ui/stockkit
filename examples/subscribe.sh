#!/bin/bash
# StockKit: Subscribe via API
# https://stockkit.net

curl -X POST https://stockkit.net/api/subscribe \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "market": "US",
    "stocks": ["NVDA", "AAPL", "TSLA"],
    "deliveryTime": "after_close",
    "locale": "en"
  }'
