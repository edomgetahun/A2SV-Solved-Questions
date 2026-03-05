t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    prefix1 = [0] * n   # for the red 
    curr = 0
    for i in range(len(prefix1)):
        curr += red[i]
        prefix1[i] = curr
    val1 = max(max(prefix1), 0)

    prefix2 = [0] * m   # for the blue 
    curr = 0
    for j in range(len(prefix2)):
        curr += blue[j]
        prefix2[j] = curr
    val2 = max(max(prefix2), 0)
    
    print(max(0, val1+val2))