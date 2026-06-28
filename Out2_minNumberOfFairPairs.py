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

"""
| Aspect               | Answer                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Binary Search (`bisect_left` and `bisect_right`)**                                                                                                                                  |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and for each of the `n` elements, two binary searches take **O(log n)** each. Overall: **O(n log n)**.                                           |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                         |
| **Is it Optimal?**   | **Yes.** This is an optimal solution. An equivalent optimal approach is **Sorting + Two Pointers**, which also runs in **O(n log n)** time (dominated by sorting) and **O(1)** auxiliary space. |

"""