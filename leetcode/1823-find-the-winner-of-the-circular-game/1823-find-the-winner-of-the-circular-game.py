class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for num in range(1, n+1):
            queue.append(num)

        while len(queue) > 1:
            for num in range(k-1): # remove k-1 times from the list and append it to the last
                queue.append(queue.popleft())
            queue.popleft() # the one we want to remove
        return queue[0]


        



