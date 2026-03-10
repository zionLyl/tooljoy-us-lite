"""美股指数快照。Usage: python3 us_snapshot.py"""
import json, yfinance as yf

def us_indices():
    tickers = {"SPY": "S&P 500", "QQQ": "Nasdaq 100", "DIA": "Dow Jones", "^VIX": "VIX"}
    results = []
    for sym, name in tickers.items():
        try:
            h = yf.Ticker(sym).history(period="2d")
            if h.empty: continue
            price = float(h["Close"].iloc[-1])
            prev = float(h["Close"].iloc[-2]) if len(h)>1 else price
            results.append({"name": name, "symbol": sym, "price": round(price,2), "change_pct": round((price/prev-1)*100,2)})
        except: continue
    return results

if __name__ == "__main__":
    print(json.dumps({"source": "yfinance", "tier": "free", "indices": us_indices()}, indent=2, ensure_ascii=False))
