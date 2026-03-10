# 🔧 ToolJoy US Lite — Free

US stock real-time quotes + basic technical analysis. Zero cost.

## What You Get

Ask your AI "How's NVDA doing?":

```
🔧 NVIDIA Corporation (NVDA)
━━━━━━━━━━━━━━━━━━━━
💰 $182.65 (+2.72%)
📊 Technicals
  RSI(14): 38.2
  MACD: Bearish
  SMA50: $128.94 (above ✅)
  Support: $102.21 | Resistance: $143.07
📈 Fundamentals
  Market Cap: $4,439.3B
  PE: 37.3
━━━━━━━━━━━━━━━━━━━━
🔧 ToolJoy Lite
```

Ask "US market snapshot":

```
📊 US Index Snapshot
  S&P 500 (SPY)   $598.41  +0.87%
  Nasdaq 100 (QQQ) $512.33  +1.24%
  Dow Jones (DIA)  $425.17  +0.52%
  VIX              $23.41   -3.20%
```

## Install

Tell your OpenClaw AI:
> "Install this Skill: https://github.com/zionLyl/tooljoy-us-lite"

Dependencies: `pip install yfinance pandas numpy`

## Data Source

| Source | Cost | Notes |
|---|---|---|
| Yahoo Finance (yfinance) | Free | No API key needed |

---

## 🔧 ToolJoy US Full Product Line

### Basic
**19 sector ETFs** (11 SPDR + 8 thematic) + **7 financial stress indicators** + **options P/C ratio**

Ask "Which sectors are strong?":
```
🏭 US Sector Analysis (19 ETFs)
━━━━━━━━━━━━━━━━━━━━
Trend Score (5-point scale):

🟢 XLU  Utilities     4.2  强势  20d: +8.3%
🟢 XLE  Energy        3.8  强势  20d: +5.1%
🟢 XLC  Comm Services 3.5  强势  20d: +4.7%
🟡 XLK  Technology    2.8  中性  20d: +1.2%
🔴 XLRE Real Estate   1.2  弱势  20d: -3.4%

🚦 Financial Stress (1/7 red)
  VIX: 23.4 ✅ | Term Structure: Inverted ⚠️
  Credit Spread: Normal ✅ | Yield Curve: Normal ✅
  Gold: Neutral ✅ | USD: Neutral ✅ | Breadth: OK ✅
```

### Pro
**Strategy signal engine** + **quantitative stock picker** (500+ stocks) + **news sentiment AI scoring** + **visual dashboard**

Ask "Run full US report":
```
🔧 ToolJoy US Trading Report
━━━━━━━━━━━━━━━━━━━━
🕐 2026-03-10 | SMH

📊 Strategy Signal: HOLD
  • 252d Momentum: +75.8% bullish
  • Price < SMA50 ⚠️
  • MACD: Death cross ⚠️
  • RSI: 41.2 neutral

🚦 Financial Stress (1/7 red) → PASS
📰 Sentiment: NEUTRAL (+0.1)

🏭 Sector Rotation (4/11 strong)
  Strong: Utilities, Energy, Comm, Healthcare
  Weak: Real Estate, Consumer Disc

🎯 Decision: HOLD — momentum strong but
   technical weakness, wait for confirmation
```

Ask "Update dashboard":

> Receive a full dark-theme visual dashboard screenshot (strategy panel, stress gauge, sector heatmap, market snapshot cards)

### Advanced
**6 backtesting strategies** + **multi-strategy comparison** + **SEC EDGAR filings** + **options Greeks**

Ask "Backtest momentum strategy, US, last 6 months":
```
📊 Backtest: Momentum (US)
━━━━━━━━━━━━━━━━━━━━
  Total Return:   +10.26%
  Annualized:     +10.26%
  Sharpe Ratio:   0.50
  Max Drawdown:   -9.18%
  Win Rate:       61.1%
  Total Trades:   18
  Profit Factor:  1.72
  Benchmark (SPY): +16.92%
```

Ask "Compare all strategies":
```
📊 6-Strategy Comparison
Strategy          Annual  Sharpe  MaxDD   WinRate
Momentum          +10.3%  0.50   -9.2%   61%
Mean Reversion    +28.9%  2.43   -3.0%   72%
Trend Follow      +14.2%  0.88   -7.1%   55%
Volatility Break  +18.7%  1.34   -5.5%   58%
Multi-Factor      +16.1%  1.15   -4.8%   63%
Sector Rotation   +12.5%  0.79   -8.4%   49%
```

### Ultimate
**Full automation**: 4 daily reports auto-pushed + **Alpaca paper trading** + **options flow alerts** + **Congress trade tracking** + **factor optimizer** + full source code

Your AI runs automatically, you do nothing:
```
[Pre-market]  📢 Market brief → pushed to Telegram/Feishu
[Open]        📢 Opening report + strategy signals
[Midday]      📢 Midday update
[Close]       📢 Full summary + dashboard screenshot

[Portfolio Monitor]
⚠️ BX down -7.8%, soft stop triggered — reduce half?
🔔 APP up +19.4%, trailing stop — lock profits

[Unusual Activity]
🐋 NVDA: Large call sweep $200 strike, 3/21 exp
   Volume 12x avg — someone knows something?

[Congress Trades]
🏛️ Nancy Pelosi bought NVDA calls (filed 3/8)

[Auto-Rebalance]
Strategy picks vs holdings → suggestions → you confirm → Alpaca executes
```

---

> 📱 Upgrade: **WeChat LylZymm** | **小红书 工具使我快乐**
>
> 🇨🇳 A股用户？看 [tooljoy-cn-lite](https://github.com/zionLyl/tooljoy-cn-lite)

## License
MIT
