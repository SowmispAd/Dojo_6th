def subsetsWithDup(nums):
    nums.sort()
    result = []
    def backtrack(start,path):
        result.append(path[:])
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0,[])
    return result
nums = list(map(int,input().split()))
print(subsetsWithDup(nums))


"""
| Aspect               | Answer                                                                                                                                                                                                                                             |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Sorting + Duplicate Skipping**                                                                                                                                                                                              |
| **Time Complexity**  | **O(n × 2ⁿ)** – There are up to `2ⁿ` unique subsets, and copying each subset into the result takes up to **O(n)**. Sorting contributes **O(n log n)** but is dominated by subset generation.                                                       |
| **Space Complexity** | **O(n)** auxiliary – Recursion stack and current `path` require **O(n)** space (excluding the output list).                                                                                                                                        |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all unique subsets, the output size itself can be **Θ(n × 2ⁿ)** in the worst case. The sorting + backtracking approach with duplicate skipping is the standard and asymptotically optimal solution. |

"""