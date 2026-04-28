t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    total = (n*(n-1)*(n-2))//6
    for r in range(n-1, 1, -1):
        l , m = 0, r-1
        while l < m :
            if a[l] + a[m] <= a[r] or a[l] + a[m] + a[r] <= a[-1] :
                total -= (m - l )
                l += 1
            else:
                m -= 1
    print(total)