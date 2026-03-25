s = input()
stack = [-1]        # we start from -1 so we can track a valid string which start from index 0 
max_len = cnt = 0
for i, ch in enumerate(s):
    if ch == "(":
        stack.append(i)
    else:
        stack.pop()
        
        if not stack:
            stack.append(i)     # reset the base
        else:
            length = i - stack[-1] 
            if length > max_len:
                max_len = length
                cnt = 1
            elif length == max_len:
                cnt += 1

if max_len == 0:
    cnt = 1
print(max_len, cnt)