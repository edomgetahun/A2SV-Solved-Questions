test = int(input())
for _ in range(test):
    n , x, k = map(int, input().split())
    s = input()

    found = False
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        else:
            x += 1
        k -= 1
        if x == 0:
            found = True
            break
    
    if not found:
        print(0)
        continue

  
    ans = 1
    t = 0
    found = False
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        else:
            x += 1
        t += 1
        if x == 0:
            found = True
            break

    if found:
        ans += k // t
    print(ans)


    
    
