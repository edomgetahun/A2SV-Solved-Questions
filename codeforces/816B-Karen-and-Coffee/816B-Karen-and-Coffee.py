# count = [0] * (200001)
# for l, r in recipe:
#     for temp in range(l, r + 1):
#         count[temp] += 1
isAdmissible = []
for j in range(len(prefix)):
    if prefix[j] >= k:
        isAdmissible.append(1)
    else:
        isAdmissible.append(0)

total = 0
for i in range(len(isAdmissible)):
    total += isAdmissible[i]
    isAdmissible[i] = total


for que in range(q):
    a , b = map(int, input().split())
    cnt = isAdmissible[b] - isAdmissible[a-1]
    print(cnt)