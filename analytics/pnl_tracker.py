# analytics/pnl_tracker.py

class PnLTracker:
    def __init__(self):
        self.trades = []
        self.total_profit = 0.0
        self.total_cost = 0.0
        self.wins = 0
        self.losses = 0

    def record_trade(self, entry_price, exit_price, size, side, signal):
        if entry_price is None or exit_price is None:
            print("[pnl] Missing price data.")
            return

        profit = 0
        if side == "BUY":
            profit = (exit_price - entry_price) * size
        elif side == "SELL":
            profit = (entry_price - exit_price) * size

        self.total_profit += profit
        self.total_cost += entry_price * size

        if profit > 0:
            self.wins += 1
        elif profit < 0:
            self.losses += 1

        trade = {
            "entry": entry_price,
            "exit": exit_price,
            "size": size,
            "side": side,
            "signal": signal,
            "profit": round(profit, 6)
        }
        self.trades.append(trade)
        print(f"[pnl] Trade recorded: {trade}")

    def get_summary(self):
        roi = (self.total_profit / self.total_cost) * 100 if self.total_cost > 0 else 0
        return {
            "total_profit": round(self.total_profit, 6),
            "roi_percent": round(roi, 2),
            "wins": self.wins,
            "losses": self.losses,
            "total_trades": len(self.trades)
        }
