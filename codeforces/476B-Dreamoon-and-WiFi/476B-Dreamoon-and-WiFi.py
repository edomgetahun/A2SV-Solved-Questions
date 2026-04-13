def dfs(i, poss):
        global valid

        if i == unk: 
            if poss == f:
                valid += 1
            return
        dfs(i+1, poss+1)
        dfs(i+1, poss-1)
    dfs(0, cur)
    print("{:.12f}".format(valid / total))