from pytrends.request import TrendReq
import time

class GoogleTrendEntropy:
    def __init__(self, keyword="bitcoin", region="SG", interval="now 1-H"):
        self.keyword = keyword
        self.region = region
        self.interval = interval
        self.name = "google_trend"

        self.last_entropy = 0.0
        self.last_update_time = 0
        self.cooldown_seconds = 300  # 5-minute cooldown

        self.pytrends = TrendReq(hl="en-US", tz=360)

    def update(self):
        # Throttle requests to avoid 429 errors
        if time.time() - self.last_update_time < self.cooldown_seconds:
            return self.last_entropy

        try:
            self.pytrends.build_payload([self.keyword], geo=self.region, timeframe=self.interval)
            data = self.pytrends.interest_over_time()
            if data.empty:
                return self.last_entropy

            latest = data[self.keyword].iloc[-1]
            self.last_entropy = round(float(latest), 4)
            self.last_update_time = time.time()
            return self.last_entropy

        except Exception as e:
            print(f"[google_trend] Error: {e}")
            self.last_entropy = 0.0  # Fallback value
            self.last_update_time = time.time()  # Prevent retry storm
            return self.last_entropy

    def get_entropy(self):
        return self.last_entropy

    def get_metadata(self):
        return {
            "name": self.name,
            "keyword": self.keyword,
            "region": self.region,
            "interval": self.interval,
            "last_entropy": self.last_entropy,
            "last_update_time": self.last_update_time
        }
