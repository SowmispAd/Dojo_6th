def findSubsequence(nums):
    res = []
    path = []
    def backtrack(start):
        if len(path) >= 2:
            res.append(path[:])
        used = set()
        for i in range(start,len(nums)):
            if nums[i] in used:
                continue
            if path and nums[i]<path[-1]:
                continue
            used.add(nums[i])
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
    backtrack(0)
    return res
nums = list(map(int,input().split()))
res = findSubsequence(nums)
for i in res:
    print(*i)


"""
| Aspect               | Answer                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Hash Set for Duplicate Elimination**                                                                                                                                                                                              |
| **Time Complexity**  | **O(n × 2ⁿ)** – There are up to `2ⁿ` recursive states (all subsets), and copying each valid subsequence into the result takes up to **O(n)**.                                                                                                            |
| **Space Complexity** | **O(n)** auxiliary – Recursion stack and current `path` require **O(n)** space (excluding the output list).                                                                                                                                              |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all non-decreasing subsequences, the output itself can be exponential in size. Any algorithm must spend at least **O(total output size)** time, making this backtracking approach asymptotically optimal. |

"""