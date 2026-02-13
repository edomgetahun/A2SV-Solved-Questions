matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

r , c = 2, 2
swaps = 0
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            swaps += abs(r-i) + abs(c-j)
            found = True
            break
    if found:
        break
print(swaps)
