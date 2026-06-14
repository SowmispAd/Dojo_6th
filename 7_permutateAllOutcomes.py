def permutate(nums):
    nums.sort()
    res = []
    used = [False]*len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return 
        for i in range (len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res
nums = list(map(int,input().split()))
res = permutate(nums)
print(*res)