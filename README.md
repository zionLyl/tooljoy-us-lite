# 🔧 ToolJoy US Stock Research

> AI + quantitative data, one sentence to get a full research report. Built over 3 months of real debugging — just install and use.

## Product Line Overview

| Tier | What It Does | Data Sources | Key Capabilities |
|---|---|---|---|
| **Lite** (this repo) | Try AI stock research | 1 (yfinance) | Quote + technicals + index snapshot |
| **Standard** | From single stocks → understand the market | 6 | + 19 sectors + stress monitor + screener + dashboard |
| **Full** | Institutional research + full automation | 12 | + DCF + backtest + reports + paper trading + full source |

> 📱 Upgrade: **WeChat LylZymm** ｜ **小红书 工具使我快乐**

---

## Lite — Free (This Repo)

**Data Source**: Yahoo Finance (yfinance) — free, no API key needed

Ask your AI **"How's NVDA doing?"**:

```
🔧 NVIDIA Corporation (NVDA)
━━━━━━━━━━━━━━━━━━━━
💰 $182.65 (+2.72%)
📊 Technicals
  RSI(14): 38.2 | MACD: Bearish
  SMA50: $128.94 (above ✅)
  Support: $102.21 | Resistance: $143.07
📈 Market Cap: $4,439.3B | PE: 37.3
━━━━━━━━━━━━━━━━━━━━
🔧 ToolJoy Lite
```

Ask **"US market snapshot"**:

```
📊 US Index Snapshot
  S&P 500 (SPY)   $598.41  +0.87%
  Nasdaq 100 (QQQ) $512.33  +1.24%
  Dow Jones (DIA)  $425.17  +0.52%
  VIX              $23.41   -3.20%
```

### Install

Tell your OpenClaw AI:
> "Install this Skill: https://github.com/zionLyl/tooljoy-us-lite"

Dependencies: `pip install yfinance pandas numpy`

---

## Standard

> **From watching stocks to understanding the entire market and finding opportunities**

### What's New vs Lite

| New Capability | Details |
|---|---|
| **19 ETF Sector Analysis** | 11 SPDR + 8 thematic (SMH, IGV, IBB, ARKK...), multi-timeframe scoring |
| **7 Financial Stress Indicators** | VIX + term structure + credit spread + yield curve + gold + USD + breadth |
| **Options P/C Ratio** | Market-wide put/call sentiment |
| **Strategy Signal Engine** | Momentum + RSI + SMA50 + MACD composite scoring |
| **Full-Market Screener** | 500+ stocks, 5-factor quantitative ranking |
| **Visual Dashboard** | Dark theme, sector heatmap + strategy panel + stress gauge |
| **Earnings Analysis** | Revenue/income/margins/YoY + consensus estimates |
| **News Digest** | Finnhub + NewsAPI dual-source aggregation |

### Data Sources (6)

| Source | Cost | Capability |
|---|---|---|
| yfinance | Free | Quotes + financials + options chain |
| Alpha Vantage | Free 25/day | Technical indicators + forex |
| Finnhub | Free 60/min | Real-time + company news + analyst ratings |
| FMP | Free 250/day | DCF valuations + ETF holdings + grades |
| Twelve Data | Free 800/day | Real-time + reference data |
| NewsAPI | Free 100/day | Global news aggregation |

### What You'll See

Ask **"Which sectors are strong?"**:

```
🏭 US Sector Analysis (19 ETFs)
━━━━━━━━━━━━━━━━━━━━
🟢 XLU  Utilities     4.2  Strong   20d: +8.3%
🟢 XLE  Energy        3.8  Strong   20d: +5.1%
🟢 XLC  Comm Services 3.5  Strong   20d: +4.7%
🟡 XLK  Technology    2.8  Neutral  20d: +1.2%
🔴 XLRE Real Estate   1.2  Weak     20d: -3.4%

🚦 Financial Stress (1/7 red) → PASS
  VIX: 23.4 ✅ | Term: Inverted ⚠️ | Credit: ✅
  Yield Curve: ✅ | Gold: ✅ | USD: ✅ | Breadth: ✅
```

Ask **"NVDA earnings analysis"**:

```
📊 NVIDIA Earnings Analysis
━━━━━━━━━━━━━━━━━━━━
Revenue: $215.9B (+65.5% YoY)
Net Income: $72.8B (+145.2%)
Gross Margin: 73.0% | Operating Margin: 61.1%
ROE: 101.5% | Free Cash Flow: $60.9B

Analyst Consensus: Strong Buy (42/45)
Price Target: $175 (current: $182.65)
```

---

## Full

> **Institutional-grade research + full automation. Saves you 2-3 months of development.**

### What's New vs Standard

| New Capability | Details |
|---|---|
| **DCF Valuation** | 5-year FCF projection + WACC sensitivity matrix (5×3) |
| **Peer Comparison (Comps)** | Auto-match peer group, 6-dimension comparison table |
| **Deep Research Report** | One command → full 8-dimension research report |
| **Catalyst Calendar** | Earnings / dividends / FOMC / CPI / options expiry |
| **Institutional Holdings** | Top holders (Vanguard/BlackRock) + insider transactions |
| **Anomaly Signals** | Large options flow + insider moves + unusual volume |
| **6 Backtest Strategies** | Momentum / mean reversion / trend follow / vol breakout / multi-factor / sector rotation |
| **Factor Optimizer** | Grid search (~200 combos) + genetic algorithm |
| **Alpaca Paper Trading** | $100K paper account, one-click orders + auto-rebalance |
| **Auto Push** | 4x daily → Telegram |
| **Stop-loss Alerts** | Soft -5% / hard -8% |
| **Options Flow** | Unusual Whales — sweeps, dark pool, whale trades |
| **Congress Trades** | Quiver Quant — track what Congress is buying |
| **PDF Report Export** | Markdown → professionally formatted PDF |
| **Full Source Code** | ~8000 lines Python, fully modifiable |

### Data Sources (all 12)

| Source | Cost | Not in Standard |
|---|---|---|
| Tiingo | Free 1000/day | 3-year+ deep history |
| IEX Cloud | Free 50k msg/mo | Full-market data |
| SEC EDGAR | Free | 10-K/10-Q filing full text |
| Polygon.io | $29+/mo | Tick-level real-time + options |
| Unusual Whales | $40/mo | Options flow / dark pool |
| Quiver Quant | $10/mo | Congress trades / insider / gov contracts |

> Plus all 6 from Standard = 12 total sources with smart fallback chains

### What You'll See

Ask **"Backtest mean reversion, last 6 months"**:

```
📊 Backtest: Mean Reversion (US)
━━━━━━━━━━━━━━━━━━━━
  Annual Return:  +28.89%
  Sharpe Ratio:   2.43
  Max Drawdown:   -3.0%
  Win Rate:       72.2%
  Benchmark (SPY): +16.92%
```

Ask **"Compare all strategies"**:

```
📊 6-Strategy Comparison
Strategy          Annual  Sharpe  MaxDD   WinRate
Momentum          +10.3%  0.50   -9.2%   61%
Mean Reversion    +28.9%  2.43   -3.0%   72%
Trend Follow      +14.2%  0.88   -7.1%   55%
Vol Breakout      +18.7%  1.34   -5.5%   58%
Multi-Factor      +16.1%  1.15   -4.8%   63%
Sector Rotation   +12.5%  0.79   -8.4%   49%
```

Your AI runs on autopilot:

```
[Pre-market]  📢 Market brief → Telegram
[Open]        📢 Opening signals
[Midday]      📢 Midday update
[Close]       📢 Full summary + dashboard screenshot

⚠️ BX down -7.8% → soft stop triggered
🐋 NVDA: Large call sweep $200 strike — 12x avg volume
🏛️ Nancy Pelosi bought NVDA calls (filed 3/8)
```

---

## Technical Summary

| Metric | Lite | Standard | Full |
|---|---|---|---|
| Data Sources | 1 | 6 | 12 |
| Analysis Modules | 2 | 15 | 30+ |
| Backtest Strategies | — | — | 6 |
| Sector ETFs | — | 19 | 19 |
| Stress Indicators | — | 7 | 7 |
| Institutional Modules | — | 3 | 13 |
| Code | ~200 lines | ~3000 lines | ~8000 lines |
| Automation | — | — | ✅ |
| Paper Trading | — | — | Alpaca |

## Why This Price

Not priced by feature count — priced by **how much time it saves you**:

| DIY Task | Time |
|---|---|
| Integrate 12 data sources + smart fallback | 2 weeks |
| API quirks (rate limits, timezone, encoding) | 1 week |
| 6 backtest strategies with realistic costs | 1 week |
| 9 institutional modules (DCF/Comps/catalyst...) | 2 weeks |
| Portfolio risk + optimizer + automation | 1 week |
| **Total** | **2-3 months** |

---

> 📱 Upgrade: **WeChat LylZymm** ｜ **小红书 工具使我快乐**
>
> 🇨🇳 A股用户？See [ToolJoy CN Lite](https://github.com/zionLyl/tooljoy-cn-lite)

## License
MIT
