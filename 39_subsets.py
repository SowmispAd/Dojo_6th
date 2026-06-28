def subsets(nums):
    nums.sort()
    res = []
    def backtrack0(start,path):
        res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack0(i+1,path)
            path.pop()
    backtrack0(0,[])
    return res
nums = list(map(int,input().split()))
print(subsets(nums))

"""
| Aspect               | Answer                                                                                                                                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS)**                                                                                                                                                                                               |
| **Time Complexity**  | **O(n × 2ⁿ)** – There are `2ⁿ` subsets, and copying each subset into the result takes up to **O(n)**. Sorting contributes **O(n log n)** but is dominated by subset generation.                                      |
| **Space Complexity** | **O(n)** auxiliary – Recursion stack and current `path` require **O(n)** space (excluding the output list).                                                                                                          |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all `2ⁿ` subsets, the output size itself is **Θ(n × 2ⁿ)**. Any algorithm must take at least this much time, making this backtracking solution asymptotically optimal. |

"""