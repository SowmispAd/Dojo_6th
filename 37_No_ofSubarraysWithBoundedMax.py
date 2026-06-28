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

"""
| Aspect               | Answer                                                                                                                                             |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sliding Window / Counting + Inclusion-Exclusion** (Count subarrays with maximum ≤ `right` minus count with maximum ≤ `left - 1`)                 |
| **Time Complexity**  | **O(n)** – The helper function `count()` traverses the array once and is called twice. Overall: **O(2n) = O(n)**.                                  |
| **Space Complexity** | **O(1)** – Uses only a constant number of variables.                                                                                               |
| **Is it Optimal?**   | **Yes.** Every element must be examined at least once to determine the valid subarrays, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""