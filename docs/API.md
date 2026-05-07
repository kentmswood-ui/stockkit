# StockKit API Documentation

StockKit provides free REST APIs for stock data and analysis.

## Base URL
```
https://stockkit.net/api
```

## Endpoints

### GET/POST /api/analyze
Generate an AI stock research preview.

**GET Example:**
```bash
curl "https://stockkit.net/api/analyze?symbol=NVDA"
```

**Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| symbol | string | Yes | Stock ticker (e.g., NVDA, 600519, HK00700) |

**POST Example:**
```bash
curl -X POST "https://stockkit.net/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"symbol":"NVDA"}'
```

**Response includes:**
- Quote snapshot
- Strategy score and signal
- Latest MA/MACD/RSI/Bollinger indicators
- AI-generated research analysis
- Timestamp

### Public Report Pages
Shareable report pages are available under:

```
https://stockkit.net/reports/{SYMBOL}
```

Examples:
- `https://stockkit.net/reports/NVDA`
- `https://stockkit.net/reports/600519`
- `https://stockkit.net/reports/HK00700`

### GET /api/quote
Get real-time stock quote.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| symbol | string | Yes | Stock ticker (e.g., AAPL, 600519) |
| market | string | Yes | Market: US, CN, HK |

**Example:**
```bash
curl "https://stockkit.net/api/quote?symbol=NVDA&market=US"
```

### GET /api/levels
Get support and resistance levels.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| symbol | string | Yes | Stock ticker |
| market | string | Yes | Market: US, CN, HK |

**Response includes:**
- Pivot Points (R1, R2, S1, S2)
- Fibonacci Retracement levels
- EMA reference levels
- 30-day high/low range
- Market and as-of timestamp

### GET /api/macro
Get macroeconomic indicators.

**Response includes:**
- Federal Funds Rate
- 10Y Treasury Yield
- 10Y-2Y Spread
- VIX
- GDP Growth
- CPI

### GET /api/signal
Get market mood/sentiment signal.

**Response includes:**
- Overall sentiment (bullish/neutral/bearish)
- Key market quotes
- Macro indicators
- Top news with sentiment scores

### GET /api/news
Get financial news with sentiment analysis.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| q | string | No | Search query |
| symbol | string | No | Filter by stock |

### GET /api/screener
Smart stock screener with multi-factor filtering.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| pool | string | No | Stock pool: mega_cap, tech, growth, dividend, etf |
| filter | string | No | Filter preset: value, growth, quality, momentum |

## Rate Limits
- 60 requests per minute per IP
- No API key required

## Subscribe for Daily Reports
Visit [stockkit.net](https://stockkit.net) to subscribe for free daily AI analysis reports.
