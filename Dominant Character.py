from collections import Counter
test = int(input())

for _ in range(test):
    n = int(input())
    s = input()
    found = False
                              
    for length in range(2, 8): 
        for i in range(n - length + 1):
            sub = s[i: i+ length]
            a = sub.count('a')
            b = sub.count('b')
            c = sub.count('c')

            if a > b and a > c:
               found = True
               print(length)
               break
        if found:
            break
    if not found:
        print(-1)
