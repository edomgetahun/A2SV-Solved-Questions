n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if n % 2 == 0:
    mid = n // 2 -1
    print(nums[mid])
else:
    i = n // 2
    print(nums[i])

    





