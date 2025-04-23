import time
from threading import Lock

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_checked = time.time()
        self.lock = Lock()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_checked
            self.last_checked = now

            refill = elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + refill)

            print(f"[{time.strftime('%X')}] Elapsed: {elapsed:.2f}s | Refilled: {refill:.2f} tokens | Available tokens: {self.tokens:.2f}")

            if self.tokens >= 1:
                self.tokens -= 1
                print(f"[{time.strftime('%X')}] Request allowed | Tokens left: {self.tokens:.2f}")
                return True
            else:
                print(f"[{time.strftime('%X')}]  Request denied | Not enough tokens")
                return False
