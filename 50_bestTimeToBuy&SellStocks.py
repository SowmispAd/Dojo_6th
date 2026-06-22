def maxProfit(nums):
    profit = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i - 1]:
            profit += nums[i] - nums[i - 1]
    return profit
prices = list(map(int,input().split()))
print(maxProfit(prices))