import heapq
heap = []
n = int(input())
op = 0
res = []
for _ in range(n):
    operation = input().split()
    if operation[0] == "insert":
        val = int(operation[1])
        heapq.heappush(heap, val)
        res.append(f"insert {val}")
        op += 1
    elif operation[0] == "removeMin":
        if not heap:
            heapq.heappush(heap, 0)
            res.append("insert 0")
            op += 1
        
        heapq.heappop(heap)
        res.append('removeMin')
        op += 1
    elif operation[0] == "getMin":
        val = int(operation[1])
        while heap and heap[0] < val:
            heapq.heappop(heap)
            res.append("removeMin")
            op += 1
        if not heap or heap[0] > val:     
            heapq.heappush(heap, val)
            res.append(f"insert {val}")
            op += 1
            
        res.append(f"getMin {val}")
        op += 1

print(op)
for ops in res:
    print(ops)