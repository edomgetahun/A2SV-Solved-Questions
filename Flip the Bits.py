from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    if a == b:
        print('YES')
        continue

    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    count = Counter(a)
    
    opp = flag = 0
    for i in range(n-1,-1,-1):
        # Curr calculates the current value of a[i]
        # If swapped it will get the correct value of a[i] (opp = 1), 
        # If not it won't change(opp = 0)
        curr = (a[i] + opp)%2

        if curr == b[i]:
            count[curr] -= 1
        else:
            if count[0] == count[1]:
                opp = (1 + opp)%2 
                curr = (a[i] + opp)%2
                # op =0  cu = 1  i=1
                count[curr] -= 1
            else:
                flag = 1
                break

    if flag:
        print("NO")
    else:
        print("YES")



    
                




