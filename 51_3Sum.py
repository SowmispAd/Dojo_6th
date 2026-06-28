nums = list(map(int,input().split()))
def threeSum(nums):
    nums.sort()
    res = []
    for i in range (len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left]+ nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left]==nums[left -1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res
res = threeSum(nums)
for i in res:
    print(*i)
"""
| Aspect               | Answer                                                                                                                                                                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Two Pointers**                                                                                                                                                                                     |
| **Time Complexity**  | **O(n²)** – Sorting takes **O(n log n)**, and for each element, the two-pointer search takes **O(n)**. Overall: **O(n²)**.                                                                                     |
| **Space Complexity** | **O(1)** auxiliary (excluding the output list). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                                                     |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. No algorithm with better than **O(n²)** time complexity is known for the general 3Sum problem, and the sorting + two-pointer approach is the standard optimal solution. |
"""