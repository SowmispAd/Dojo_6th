def canPartition(nums):
    total = sum(nums)
    if total%2 != 0:
        return False
    target = total // 2
    dp = [False] * (target+1)
    dp[0] = True
    for num in nums:
        for j in range  (target, num-1,-1): # remeber the ranges
            dp[j] = dp[j] or dp[j -num]
    return dp[target]
arr = list(map(int,input().split()))
print(canPartition(arr))

"""
| Aspect               | Analysis                                                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **0/1 Knapsack (Subset Sum using 1D Dynamic Programming)**                                                                         |
| **Time Complexity**  | **O(n × target)** where `target = sum(nums) / 2`                                                                                   |
| **Space Complexity** | **O(target)** (1D DP optimization)                                                                                                 |
| **Optimal?**         | **Yes** for this problem. This is the standard optimal DP solution for Partition Equal Subset Sum                                  |
| **Key Idea**         | Reduce problem to checking if a subset sums to `total/2`, and use reverse iteration to avoid recomputation (0/1 knapsack behavior) |
| **Correctness**      | Correct implementation and handles all cases efficiently                                                                           |

"""