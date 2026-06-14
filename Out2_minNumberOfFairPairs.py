import bisect
from bisect import bisect_left,bisect_right
def countFairPairs(nums,upper,lower) :
        ans = 0
        nums.sort()
        for i in range (len(nums)-1):
            min_req = lower - nums[i]
            max_req = upper - nums[i]
            low = bisect_left(nums,min_req,i+1)
            high = bisect_right(nums,max_req,i+1)
            ans += high - low
        return ans
nums = list(map(int,input().split()))
lower,upper = map(int,input().split())
print(countFairPairs(nums,lower,upper))