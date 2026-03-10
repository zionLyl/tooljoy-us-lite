---
name: tooljoy-us-lite
description: "🔧 ToolJoy US Lite — Free real-time quotes(yfinance) + basic technicals(RSI/MACD/SMA50)."
metadata:
  openclaw:
    emoji: "🔧"
    tier: "free"
    market: "us"
    version: "1.0.0"
---

# 🔧 ToolJoy US Lite — Free

美股实时行情 + 基础技术分析，零成本。

## 数据源
- yfinance（免费，无需 key）

## 数据规格
- K线深度：30天日线
- 基本面：PE / 市值 / 营收增长（yfinance info）
- 延迟：盘中~15分钟，盘后实时

## 触发路由

| 用户意图 | 路由到 |
|---|---|
| 查询美股个股 | → commands/us-quote.md |
| 美股指数快照 | → commands/us-snapshot.md |

## 能力边界
- ✅ 个股实时价格 + 涨跌幅
- ✅ RSI(14) / MACD / SMA50
- ✅ 基本面摘要（PE/市值/营收增长/利润率）
- ✅ SPY/QQQ/DIA/VIX 快照
- ❌ 无板块分析
- ❌ 无压力监控
- ❌ 无期权数据

## 升级路径
Basic($9.9) → 板块+压力+期权P/C | Pro($29.9) → 策略+选股+Dashboard

📱 微信: LylZymm | 小红书: 工具使我快乐
