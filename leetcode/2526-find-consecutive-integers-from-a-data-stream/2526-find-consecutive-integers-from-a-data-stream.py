class DataStream:
    def __init__(self, val: int, k: int):
        self.val = val
        self.k = k
        self.queue = deque()
        self.count = 0
    
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.val:
            self.count += 1
        else:
            self.count = 0

        if len(self.queue) > self.k:
            self.queue.popleft()
            
        return self.count >= self.k