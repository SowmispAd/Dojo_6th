def subsets(nums):
    nums.sort()
    res = []
    def backtrack0(start,path):
        res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack0(i+1,path)
            path.pop()
    backtrack0(0,[])
    return res
nums = list(map(int,input().split()))
print(subsets(nums))