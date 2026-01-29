from collections import defaultdict
import heapq


class StockPrice:

    def __init__(self):
        # latest timestamp and its price
        self.latest_price = 0
        self.latest_timestamp = 0

        # timestamp -> price mapping
        self.timestamp_price = {}

        # price -> frequency mapping (for lazy deletion)
        self.price_freq = defaultdict(int)

        # heaps
        self.max_heap = []   # store -price
        self.min_heap = []   # store price

    def update(self, timestamp: int, price: int) -> None:
        # if timestamp already exists, invalidate old price
        if timestamp in self.timestamp_price:
            prev_price = self.timestamp_price[timestamp]
            self.price_freq[prev_price] -= 1

            # update latest price if needed
            if timestamp == self.latest_timestamp:
                self.latest_price = price

        # if new timestamp is the latest
        elif timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
            self.latest_price = price

        # push price into heaps if first occurrence
        if self.price_freq[price] == 0:
            heapq.heappush(self.max_heap, -price)
            heapq.heappush(self.min_heap, price)

        # update mappings
        self.timestamp_price[timestamp] = price
        self.price_freq[price] += 1

    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        # remove invalid max values
        while self.price_freq[-self.max_heap[0]] == 0:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]

    def minimum(self) -> int:
        # remove invalid min values
        while self.price_freq[self.min_heap[0]] == 0:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# ---------------------------------------------------
# 🧪 Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":
    sp = StockPrice()

    sp.update(1, 10)
    sp.update(2, 5)
    print("Current:", sp.current())    # 5
    print("Maximum:", sp.maximum())    # 10
    print("Minimum:", sp.minimum())    # 5

    sp.update(1, 3)    # update previous timestamp
    print("Maximum:", sp.maximum())    # 5
    print("Minimum:", sp.minimum())    # 3

    sp.update(4, 2)
    print("Current:", sp.current())    # 2
    print("Maximum:", sp.maximum())    # 5
    print("Minimum:", sp.minimum())    # 2
