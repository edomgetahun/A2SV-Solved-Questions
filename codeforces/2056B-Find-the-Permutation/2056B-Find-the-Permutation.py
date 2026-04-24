def dfs(num):
        visited[num] = True
        for negh in adj_list[num]:
            if not visited[negh]:
                dfs(negh)
        res.append(num)

    for num in range(n):
        if not visited[num]:
            dfs(num)
    
    res.reverse()
    for  i in range(n):
        res[i] += 1
    print(*res)