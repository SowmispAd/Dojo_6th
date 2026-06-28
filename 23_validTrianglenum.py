def validTriangleNum(nums):
    nums.sort()
    n = len(nums)
    count = 0
    for k in range(n-1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += (j - i)
                j -= 1
            else:
                i += 1
    return count
nums = list(map(int,input().split()))
print(validTriangleNum(nums))

"""
| Aspect               | Answer                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Sorting + Two Pointers**                                                                                                                                                                                         |
| **Time Complexity**  | **O(n²)** – Sorting takes **O(n log n)**, and for each possible largest side, the two-pointer search takes **O(n)**. Overall: **O(n²)**.                                                                           |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                            |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. No algorithm with better than **O(n²)** time complexity is known for counting all valid triangles, and the sorting + two-pointer approach is the standard optimal solution. |

"""