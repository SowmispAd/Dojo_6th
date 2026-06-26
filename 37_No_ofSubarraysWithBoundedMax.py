def numSubarrayBoundedMax(nums, left, right):
    def count(bound):
        ans = 0
        length = 0
        for num in nums:
            if num <= bound:
                length += 1
            else:
                length = 0
            ans += length
        return ans
    return count(right) - count(left - 1)
nums = list(map(int,input().split()))
left, right = map(int,input().split())
print(numSubarrayBoundedMax(nums,left,right))