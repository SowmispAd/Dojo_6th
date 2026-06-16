def combinationSumIII(k,n):
    result = []
    def backtrack(start,path,total):
        if len(path) ==k:
            if total == n:
                result.append(path[:])
            return
        for i in range(start,10):
            if total + i > n:
                break
            path.append(i)
            backtrack(i+1,path,total+i)
            path.pop()
    backtrack(1,[],0)
    return result
k, n = map(int,input().split())
res = combinationSumIII(k,n)
print(*res)