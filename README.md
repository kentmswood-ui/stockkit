# StockKit — Free AI Stock Reports

[![Website](https://img.shields.io/badge/Website-stockkit.net-blue)](https://stockkit.net)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://stockkit.net)

> **Wall Street-grade AI stock analysis reports, delivered to your inbox daily. 100% free.**

## What is StockKit?

StockKit is a free AI-powered stock research platform that delivers institutional-grade analysis reports directly to your email. No account registration needed — just subscribe with your email and start receiving daily reports.

StockKit also provides an instant research demo on the homepage: enter a US, China A-share, or Hong Kong ticker and get a live AI analysis preview backed by quotes, technical indicators, strategy scores, and news context.

### Supported Markets
- 🇺🇸 **US Stocks** — NYSE, NASDAQ, S&P 500, Dow Jones, Nasdaq 100
- 🇨🇳 **China A-Shares** — SSE, SZSE, ChiNext, STAR Market, BSE
- 🇭🇰 **Hong Kong** — HSI, Hang Seng Tech, Stock Connect, H-Shares

### AI Models
- **Claude Opus** (Anthropic) — Deep reasoning & long-form analysis
- **Gemini Pro** (Google DeepMind) — Multimodal understanding
- **DeepSeek V3** — Strong financial comprehension
- **GLM-5** (Zhipu) — China A-shares specialist
- **GPT-4o** (OpenAI) — Global financial knowledge
- **Qwen** (Alibaba) — Best Chinese language context

### Technical Analysis Engine
- **Moving Averages**: MA(5/10/20/60)
- **MACD**: DIF, DEA, Histogram with crossover detection
- **RSI**: RSI(6) and RSI(14) with overbought/oversold alerts
- **Bollinger Bands**: Upper/Middle/Lower with bandwidth analysis
- **Volume Analysis**: Volume-price divergence detection
- **Support/Resistance**: Pivot Points, Fibonacci, EMA clusters

### Multi-Strategy Scoring
| Strategy | Signal Type |
|----------|-------------|
| MA Crossover | Trend following |
| RSI Extremes | Mean reversion |
| MACD Divergence | Momentum |
| Bollinger Squeeze | Volatility breakout |
| Volume-Price | Confirmation |

### Data Sources
| Source | Coverage |
|--------|----------|
| Alpha Vantage | Real-time quotes, historical candles, fundamentals |
| FRED | GDP, CPI, interest rates, unemployment |
| NewsAPI | Global financial news with sentiment analysis |
| Yahoo Finance | Stock quotes, financial statements, dividends |
| Sina Finance | China A-shares & HK real-time quotes |
| Tushare Pro | China A-shares historical data & financials |
| Binance | Crypto real-time and historical data |
| Polygon.io | US tick-level data, options chain, IPO calendar |

## Daily Report Contents

Each report includes:

1. **🎯 Core Takeaway** — Market sentiment, position sizing, one-line thesis
2. **📊 Global Market Overview** — US/China/HK analyzed with deep insights
3. **🔍 3 Key Drivers** — Most important events with data support
4. **📐 Technical Diagnosis** — Cross-validated signals with S/R levels
5. **⚡ Trading Plan** — Entry/stop-loss/target with risk-reward ratios
6. **⚠️ Risk Matrix** — Probability, impact, triggers, response strategies

## Live Research Demo

Try the public demo at [stockkit.net](https://stockkit.net):

- Enter `NVDA`, `AAPL`, `600519`, or `HK00700`
- Review real-time quote data, strategy score, MA/RSI/Bollinger readings
- Get an AI-generated research preview before subscribing
- Subscribe to receive complete daily reports by email

Shareable public report pages are available at:

- [stockkit.net/reports](https://stockkit.net/reports)
- [stockkit.net/reports/NVDA](https://stockkit.net/reports/NVDA)
- [stockkit.net/reports/AAPL](https://stockkit.net/reports/AAPL)
- [stockkit.net/reports/600519](https://stockkit.net/reports/600519)
- [stockkit.net/reports/HK00700](https://stockkit.net/reports/HK00700)

Public report pages are server-rendered for search engines and include structured metadata for sharing.

## How to Subscribe

1. Visit [stockkit.net](https://stockkit.net)
2. Enter your email and select a market
3. Add up to 3 stocks to watch
4. Verify your email
5. Receive daily reports automatically

**It takes 30 seconds. No account needed. 100% free.**

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS
- **AI Engine**: Multi-model adapter (Claude, Gemini, DeepSeek, GLM-5, GPT-4o)
- **Data**: Alpha Vantage, FRED, NewsAPI, Yahoo Finance
- **Email**: Resend
- **Database**: SQLite (better-sqlite3)
- **Hosting**: Docker on Ubuntu

## API Examples

### Get Real-time Quote
```bash
curl https://stockkit.net/api/quote?symbol=NVDA&market=US
```

### Get Technical Levels
```bash
curl https://stockkit.net/api/levels?symbol=AAPL&market=US
```

### Generate AI Analysis
```bash
curl -X POST https://stockkit.net/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"symbol":"NVDA"}'
```

Or use GET for public report pages and lightweight integrations:

```bash
curl "https://stockkit.net/api/analyze?symbol=NVDA"
```

### Get Market Signal
```bash
curl https://stockkit.net/api/signal
```

## Contributing

We welcome contributions! Feel free to:
- Report bugs or suggest features via Issues
- Submit Pull Requests
- Share StockKit with friends

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**[Subscribe Free →](https://stockkit.net)**

*StockKit reports are AI-generated and do not constitute investment advice. Invest responsibly.*
