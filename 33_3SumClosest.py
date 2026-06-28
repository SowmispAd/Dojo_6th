def threeSumClosest(nums,target):
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]
    for i in range (n-2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - result):
                result = total
            if total == target:
                return target
            elif total < target:
                left += 1
            else:
                right -= 1
    return result
nums = list(map(int,input().split()))

target = int(input())
print(threeSumClosest(nums,target))

"""
| Aspect               | Answer                                                                                                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Two Pointers**                                                                                                                                                                                             |
| **Time Complexity**  | **O(n²)** – Sorting takes **O(n log n)**, and for each element, the two-pointer search takes **O(n)**. Overall: **O(n²)**.                                                                                             |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                                |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. No algorithm with better than **O(n²)** time complexity is known for the general 3Sum Closest problem, and the sorting + two-pointer approach is the standard optimal solution. |

"""