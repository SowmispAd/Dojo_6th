from typing import List
from collections import defaultdict

def beautifulSubsets(nums,k):
    freq = defaultdict(int)
    count = 0
    def backtack(index):
        nonlocal count
        if index == len(nums):
            count += 1
            return
        backtack(index + 1)
        num = nums[index]
        if freq[num - k] == 0 and freq[num + k] == 0:
            freq[num] += 1
            backtack(index + 1)
            freq[num] -= 1
    backtack(0)
    return count - 1
nums = list(map(int,input().split()))
k = int(input())
print(beautifulSubsets(nums,k))

"""
| Aspect               | Answer                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Two Pointers (Sliding Window)**                                                                                                                                                     |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and the two pointers (`left` and `right`) each traverse the array at most once (**O(n)**). Overall: **O(n log n)**.                              |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                         |
| **Is it Optimal?**   | **Yes.** This is an optimal solution. Any solution must account for ordering, and sorting dominates the complexity, resulting in the optimal **O(n log n)** time with **O(1)** auxiliary space. |

"""