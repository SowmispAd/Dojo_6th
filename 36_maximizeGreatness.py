def maximizeGreatness(nums):
    nums.sort()
    ans = 0
    for num in nums:
        if nums[ans] < num:
            ans+= 1
    return ans
nums = list(map(int,input().split()))
print(maximizeGreatness(nums))

"""
| Aspect               | Answer                                               |
| -------------------- | ---------------------------------------------------- |
| **Approach**         | Sorting + Two Pointers (Greedy)                      |
| **Time Complexity**  | **O(n log n)**                                       |
| **Space Complexity** | **O(1)** *(excluding Python's sort auxiliary space)* |
| **Optimized?**       | **Yes**                                              |

"""