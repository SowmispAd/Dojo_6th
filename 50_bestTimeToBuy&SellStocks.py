def maxProfit(nums):
    profit = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i - 1]:
            profit += nums[i] - nums[i - 1]
    return profit
prices = list(map(int,input().split()))
print(maxProfit(prices))

"""
| Metric               | Value                                    |
| -------------------- | ---------------------------------------- |
| **Approach**         | Greedy (Accumulate Positive Differences) |
| **Time Complexity**  | **O(n)**                                 |
| **Space Complexity** | **O(1)**                                 |
| **Optimal?**         | **Yes**                                  |


"""