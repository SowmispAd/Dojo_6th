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
| Aspect               | Answer                                                                                                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | Backtracking (Recursion) + Hash Map (`defaultdict`)                                                                                                                               |
| **Time Complexity**  | **O(2ⁿ)** – For each element, there are two choices: include or exclude. In the worst case, almost all subsets are explored.                                                      |
| **Space Complexity** | **O(n)** – Due to recursion stack (depth `n`) and the frequency map, which can store up to `n` distinct elements.                                                                 |
| **Is it Optimal?**   | **Yes.** Since the problem requires counting valid subsets and there can be up to `2ⁿ` subsets, exponential time is unavoidable in the worst case for this backtracking approach. |

"""