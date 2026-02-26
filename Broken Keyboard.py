t = int(input())
for _ in range(t):
    s = input()

    l = 0
    work = set()
    while l < len(s):
        r = l
        while r < len(s) and s[r] == s[l]: 
            r += 1
        length = r - l 
        if length % 2 == 1:
            work.add(s[l])
        l = r
    print("".join(sorted(work)))

