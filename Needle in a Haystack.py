from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    
    scount = Counter(s) 
    t = list(t)
    count = Counter(t)
    
    flag = 1
    for ch in scount:
        if count[ch] < 1:
            flag = 0
            break
    if not flag:
        print("Impossible")
        continue

    t = []
    found = False
    for ch in count:
        if ch in scount :
            if count[ch] >= scount[ch]:
                count[ch] -= scount[ch]
                found = True
            else:
                found = False
                break
        t.extend([ch] * (count[ch]))
   
    if not found:
        print("Impossible")
        continue

    
    t.sort()
    l , r = 0 , 0
    ans = []
    while l < len(t) and r < len(s):
        if t[l] < s[r]:
            ans.append(t[l])
            l += 1
        else:
            ans.append(s[r])
            r += 1
    ans.extend(t[l:])
    ans.extend(s[r:])
    print("".join(ans))

