"""美股个股查询 — Lite版：yfinance单源。Usage: python3 us_quote.py NVDA"""
import json, sys
import numpy as np, pandas as pd, yfinance as yf

def calc_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0); loss = -delta.clip(upper=0)
    ag = gain.ewm(alpha=1/period, min_periods=period).mean()
    al = loss.ewm(alpha=1/period, min_periods=period).mean()
    return 100 - (100 / (1 + ag/al))

def calc_macd(prices, fast=12, slow=26, signal=9):
    ef = prices.ewm(span=fast, adjust=False).mean()
    es = prices.ewm(span=slow, adjust=False).mean()
    macd = ef - es; sig = macd.ewm(span=signal, adjust=False).mean()
    return macd, sig, macd - sig

def query(ticker):
    t = yf.Ticker(ticker)
    hist = t.history(period="1mo")
    info = t.info or {}
    if hist.empty: return {"symbol": ticker, "error": "No data"}
    close = hist["Close"]; price = float(close.iloc[-1])
    prev = float(close.iloc[-2]) if len(close)>1 else price
    tech = {}
    if len(close) >= 20:
        rsi = calc_rsi(close); macd_l, sig_l, hist_l = calc_macd(close)
        tech = {
            "rsi_14": round(float(rsi.iloc[-1]),1) if len(close)>=14 else None,
            "macd_bullish": float(macd_l.iloc[-1])>float(sig_l.iloc[-1]) if len(close)>=26 else None,
            "support": round(float(close.tail(20).min()),2),
            "resistance": round(float(close.tail(20).max()),2),
        }
    return {
        "source": "yfinance", "tier": "free", "symbol": ticker,
        "name": info.get("shortName", ticker), "price": round(price,2),
        "change_pct": round((price/prev-1)*100,2),
        "market_cap_b": round(info.get("marketCap",0)/1e9,1) if info.get("marketCap") else None,
        "pe": round(info.get("trailingPE",0),1) if info.get("trailingPE") else None,
        **tech,
    }

if __name__ == "__main__":
    print(json.dumps(query(sys.argv[1] if len(sys.argv)>1 else "NVDA"), indent=2, ensure_ascii=False))
