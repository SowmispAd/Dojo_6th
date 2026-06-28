def maxOperations(nums,k):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0
    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            right -= 1
            left += 1
            count += 1
        elif total<k:
            left += 1
        else:
            right -= 1
    return count

"""
| Aspect                          | Analysis                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Approach Used**               | **Two Pointers after Sorting (Greedy Pairing)**                                                        |
| **Time Complexity**             | **O(n log n)** (due to sorting)                                                                        |
| **Space Complexity**            | **O(1)** auxiliary (ignoring sort’s internal space)                                                    |
| **Optimal?**                    | **Yes (for sorting-based solution)**. However, an **O(n)** optimal alternative exists using a hashmap. |
| **Key Idea**                    | Sort array, then use two pointers to greedily match pairs summing to `k`                               |
| **Alternative Better Approach** | **HashMap frequency approach gives O(n) time complexity** without sorting                              |

"""