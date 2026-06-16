
def permutaionsUnique(nums):
    nums.sort()
    res = []
    used = [False]*len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] :
                continue 
            if i >0 and nums[i] == nums[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res
nums = list(map(int,input().split()))
print(permutaionsUnique(nums))