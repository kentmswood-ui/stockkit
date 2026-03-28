# Technical Indicators Reference

StockKit calculates and cross-validates 20+ technical indicators for every analysis.

## Trend Indicators

### Moving Averages (MA)
- **MA5**: 5-day short-term trend
- **MA10**: 10-day short-term trend
- **MA20**: 20-day medium-term trend
- **MA60**: 60-day long-term trend
- **Alignment Detection**: Bullish (descending order) / Bearish (ascending order)

### MACD
- **DIF Line**: 12-EMA minus 26-EMA
- **DEA Line**: 9-period EMA of DIF
- **Histogram**: DIF minus DEA
- **Signals**: Golden Cross (buy) / Death Cross (sell)

## Momentum Indicators

### RSI (Relative Strength Index)
- **RSI(14)**: Standard period for swing trading
- **RSI(6)**: Short period for day trading
- **Zones**: Overbought (>70) / Neutral (30-70) / Oversold (<30)

## Volatility Indicators

### Bollinger Bands
- **Upper Band**: Middle + 2σ
- **Middle Band**: 20-period SMA
- **Lower Band**: Middle - 2σ
- **Bandwidth**: Measures volatility expansion/contraction
- **%B Position**: Current price position within bands

## Volume Indicators
- **Volume MA**: 20-day volume moving average
- **Volume Ratio**: Current vs average volume
- **Volume-Price Divergence**: Detects weakening trends

## Support & Resistance
- **Pivot Points**: Classic floor trader pivots
- **Fibonacci Retracement**: 23.6%, 38.2%, 50%, 61.8%, 78.6%
- **EMA Clusters**: Dynamic support/resistance from EMA convergence
- **30-Day Range**: Recent high/low boundaries

---

Learn more at [stockkit.net](https://stockkit.net)
