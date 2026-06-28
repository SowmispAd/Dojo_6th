def combinationSum2(candidates,target):
    candidates.sort()
    res = []
    def backtrack(start,path,total):
        if total == target:
            res.append(path[:])
            return
        
        if total > target:
            return 
        
        for i in range(start,len(candidates)):
            if i > start and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i+1, path, total + candidates[i])
            path.pop()
    backtrack(0,[],0)
    return res
candidates = list(map(int,input().split()))
target = int(input())
print(combinationSum2(candidates,target))

"""
| Aspect               | Answer                                                                                                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Sorting + Duplicate Skipping**                                                                                                                                                                                             |
| **Time Complexity**  | **O(2ⁿ × n)** – In the worst case, all subsets are explored (`2ⁿ`), and copying each valid combination to the result takes up to **O(n)**. Sorting contributes **O(n log n)** but is dominated by the backtracking.                               |
| **Space Complexity** | **O(n)** auxiliary – Recursion stack and current `path` require **O(n)** space (excluding the output list).                                                                                                                                       |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all unique valid combinations, the number of possible outputs can be exponential. The sorting + backtracking approach with duplicate skipping is the standard and asymptotically optimal solution. |

"""