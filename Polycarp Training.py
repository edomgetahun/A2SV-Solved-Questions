n = int(input())
con = list(map(int, input().split()))
con.sort()
day = 1
cnt = 0
for prob in con:
    if prob >= day:
        cnt += 1
        day += 1

print(cnt)
    





