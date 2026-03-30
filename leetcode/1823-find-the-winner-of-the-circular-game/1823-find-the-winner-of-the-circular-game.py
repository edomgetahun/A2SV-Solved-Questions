class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # queue = deque()
        # for num in range(1, n+1):
        #     queue.append(num)

        # while len(queue) > 1:
        #     for num in range(k-1): # remove k-1 times from the list and append it to the last
        #         queue.append(queue.popleft())
        #     queue.popleft() # the one we want to remove
        # return queue[0]

        # Recursison
        def helper(n, k):
            if n == 1:
                return 0
            return (helper(n-1,k)+ k ) % n
        return helper(n, k) + 1

        # Recursively get the winner's index from the smaller circle (n-1 people)
        # Then "shift" that index to match the current circle of size n
        # - Add k to move forward k steps
        # - Use modulo n to wrap around the circular structure
   

        



