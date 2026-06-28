def canPartition(nums):
    total = sum(nums)
    if total%2 != 0:
        return False
    target = total // 2
    dp = [False] * (target+1)
    dp[0] = True
    for num in nums:
        for j in range  (target, num-1,-1):
            dp[j] = dp[j] or dp[j -num]
    return dp[target]
arr = list(map(int,input().split()))
print(canPartition(arr))

"""
Summary
Approach: Dynamic Programming (0/1 Knapsack / Space-Optimized Subset Sum)
Time Complexity: O(n × target), where target = totalSum / 2
Space Complexity: O(target)

"""