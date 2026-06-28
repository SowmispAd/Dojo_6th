def combinationSum(candidates,target):
    res = []
    def backtrack(start,path,total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(i,path,total+candidates[i])
            path.pop()
    backtrack(0,[],0)
    return res
candidates  = list(map(int,input().split()))
target = int(input())
print(combinationSum(candidates,target))

"""
| Aspect               | Analysis                                                                                                                                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS)**                                                                                                                                                                                                            |
| **Time Complexity**  | **O(2ⁿ × n)** in the worst case (generating all subsets and copying valid paths)                                                                                                                                                  |
| **Space Complexity** | **O(n)** auxiliary space for recursion stack and current path (excluding output). Including output: **O(n × 2ⁿ)** in the worst case.                                                                                              |
| **Optimal?**         | **Yes**, for generating all valid combinations. Since every possible subset may need to be explored in the worst case, **O(2ⁿ)** is asymptotically optimal.                                                                       |
| **Note**             | This implementation solves the **Combination Sum II (each element used at most once)** variant because it calls `backtrack(i + 1, ...)`. It does **not** solve the original Combination Sum problem where elements can be reused. |

"""