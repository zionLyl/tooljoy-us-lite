# 🔧 ToolJoy US Stock Research

> AI + quantitative data, one sentence to get a full research report. 139 scripts across 3 markets — this is the free US edition.

## Two Tiers

| Tier | What It Does | Scripts | Data Sources | Key Capabilities |
|---|---|---|---|---|
| **Lite** (this repo) | Free AI stock research | 3 | 1 | Quote + technicals + index snapshot |
| **Full** | Institutional-grade quant | 45 | 6+ | 3 strategies + 6 ML models + multi-agent + paper trading + full auto | DM for access |

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

## Full — Complete Edition (45 scripts)

> **Institutional-grade quant stack: 3 strategies + 6 ML models + multi-agent orchestration + paper trading**

### What Full Adds Over Lite

**📡 Multi-Source Data**
→ yfinance + Alpha Vantage + Finnhub + FMP + Twelve Data + NewsAPI
→ Smart fallback chain — if one source fails, auto-switch to the next

**📊 Full-Market Screening**
→ 5-factor scoring: momentum + volatility + volume-price + trend + valuation
→ 500+ stocks scanned, ranked by composite score
→ Custom factor framework (Alpha101 + user-defined, IC/IR evaluation)

**📝 Deep Research Reports**
→ Fundamentals: revenue/income/margins + PE/PB/ROE + YoY trends
→ Technicals: MA system + MACD + RSI + Bollinger + ATR
→ Flow: institutional holdings + insider transactions
→ News: multi-source aggregation + sentiment scoring
→ Health grade A-D

**🎯 3 Core Strategies**
→ 🗡️ Sector Rotation: 19 ETFs, multi-timeframe momentum
→ 🛡️ Ambush: bottom-fishing with 5-layer signal validation
→ ⚖️ Quant Screener: AND-logic composite signal, backtested

**🧠 6 ML Models**
→ Triple Barrier + Purged CV
→ LightGBM gradient boosting
→ LSTM deep learning (PyTorch)
→ Alpha101 factor library (20+ factors)
→ Risk Parity portfolio allocation
→ Regime Detection (bull/bear/sideways switching)

**📈 Backtest + Pattern + Factor Analysis**
→ Single/multi-strategy comparison + parameter sweep
→ Chart pattern recognition (head & shoulders, double bottom, wedge, triangle)
→ Factor IC/IR, quintile backtest, decay analysis
→ Signal parameter Grid Search optimization

**🤖 Multi-Agent Orchestration**
→ 5 AI roles: Sentinel → Analyst → Earnings → Strategist → Orchestrator
→ One sentence triggers full pipeline: "Analyze NVDA" → data → report → score → action

**📢 Full Monitoring Suite**
→ Capital flow: institutional vs retail, unusual volume detection
→ Commodities: oil / gas / copper / gold / silver
→ Forex: 7 currency pairs
→ News + sentiment + risk alerts + stress testing

**💰 Alpaca Paper Trading**
→ Real market simulation, auto order execution
→ Signal-driven buy/sell, scheduled rebalancing
→ Pre-market screening + post-close P&L report

**📊 Dashboard + Push Notifications**
→ Dark theme: positions / P&L / sector distribution / signals
→ Telegram auto-push
→ Cron jobs one-click deploy

### What You'll See

Ask **"Screen top 10 US stocks"**:

```
📊 US Stock Screener Top 10
━━━━━━━━━━━━━━━━━━━━
 #  Stock         Score  Signal    Sector
 1  NVDA          85.2   Strong Buy  Tech
 2  META          79.4   Strong Buy  Comm
 3  AMZN          76.1   Buy         Consumer
 4  MSFT          74.8   Buy         Tech
 ...
```

Ask **"Backtest sector rotation"**:

```
📊 Sector Rotation Backtest (1 year)
━━━━━━━━━━━━━━━━━━━━
  Annual Return:  +18.7%
  Sharpe Ratio:   1.34
  Max Drawdown:   -5.5%
  Win Rate:       58%
  Benchmark (SPY): +16.9%
```

Ask **"Compare all 6 strategies"**:

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

### Data Sources (6+, mostly free)

| Source | Capability |
|---|---|
| yfinance | Quotes + financials + options + institutional holders |
| Alpha Vantage | Technical indicators + forex (free 25/day) |
| Finnhub | Real-time + news + analyst ratings (free 60/min) |
| FMP | DCF valuations + ETF holdings (free 250/day) |
| Twelve Data | Real-time + reference data (free 800/day) |
| NewsAPI | Global news aggregation (free 100/day) |
| Alpaca | Paper trading (free signup) |

### Lite vs Full

| Metric | Lite (Free) | Full |
|---|---|---|
| Scripts | 3 | **45** |
| Data Sources | 1 | **6+** |
| Strategies | — | **3 core + 6 backtest** |
| ML Models | — | **6** |
| Full-Market Screening | — | **500+ stocks** |
| Deep Research Report | — | ✅ |
| Chart Pattern Recognition | — | ✅ |
| Factor Analysis | — | ✅ |
| Multi-Agent Orchestration | — | ✅ |
| Backtest Framework | — | ✅ |
| Paper Trading | — | **Alpaca** |
| Monitoring + Push | — | **Telegram** |
| Dashboard | — | ✅ |
| Scheduled Automation | — | ✅ |
| Code | ~200 lines | **~10,000 lines** |

---

> 📱 Want Full access / upgrade / chat: **WeChat LylZymm** ｜ **小红书 工具使我快乐**
>
> 🇨🇳 A股版？→ [ToolJoy CN Lite](https://github.com/zionLyl/tooljoy-cn-lite)
> 🇭🇰 HK版？→ DM for access

## License
MIT
