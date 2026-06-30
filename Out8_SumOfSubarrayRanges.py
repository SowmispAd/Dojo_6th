def subarrayRanges(nums):
    n = len(nums)
    ans = 0
    for i in range(n):
        smallest = nums[i]
        greatest = nums[i]
        for j in range(i,n):
            smallest = min(smallest,nums[j])
            greatest = max(greatest,nums[j])
            ans += greatest - smallest
    return ans
nums = list(map(int,input().split()))
print(subarrayRanges(nums))