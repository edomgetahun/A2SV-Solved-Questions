n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l, r = 0 , 0
pair = 0
while l < n and r < m:
    if a[l] < b[r]:
        l += 1
    elif a[l] > b[r]:
        r += 1
    else: 
        val = a[l]
        
        count_a = 0
        while l < n and a[l] == val:
            count_a += 1
            l += 1

        count_b = 0
        while r < m and b[r] == val:
            count_b += 1
            r += 1
        pair += count_a * count_b
print(pair)
