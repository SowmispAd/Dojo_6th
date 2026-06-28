def maxCandiesAllocated(candies,k):
    def can_distribute(x):
        count = 0
        for pile in candies:
            count += pile //x
        return count >= k
    left, right = 1, max(candies)
    ans = 0
    while left<= right:
        mid = (left + right) // 2
        if can_distribute(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
candies = list(map(int,input().split()))
k = int(input())
print(maxCandiesAllocated(candies,k))

"""
| Aspect               | Answer                                     |
| -------------------- | ------------------------------------------ |
| **Approach**         | Binary Search on Answer                    |
| **Time Complexity**  | **O(n log M)**, where **M = max(candies)** |
| **Space Complexity** | **O(1)**                                   |
| **Optimized?**       | **Yes**                                    |

"""