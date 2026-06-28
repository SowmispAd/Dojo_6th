"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

"""

def longestOnes(nums,k):
    left = 0
    n = len(nums)
    zeros = 0
    max_len = 0
    for right in range(n):
        if nums[right] == 0:
            zeros += 1
        while zeros>k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len,right-left+1)
    return max_len

n = int(input())
nums = list(map(int,input().split()))
k = int(input())
print(longestOnes(nums,k))

"""
| Aspect               | Answer                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sliding Window (Two Pointers) + Greedy**                                                                                                      |
| **Time Complexity**  | **O(n)** – Each element is visited at most twice (once by `right`, once by `left`).                                                             |
| **Space Complexity** | **O(1)** – Uses only a fixed number of variables (`left`, `zeros`, `max_len`).                                                                  |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every element must be processed at least once, so **O(n)** time and **O(1)** space is the best possible. |

"""