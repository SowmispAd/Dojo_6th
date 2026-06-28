def combinationSumIII(k,n):
    result = []
    def backtrack(start,path,total):
        if len(path) ==k:
            if total == n:
                result.append(path[:])
            return
        for i in range(start,10):
            if total + i > n:
                break
            path.append(i)
            backtrack(i+1,path,total+i)
            path.pop()
    backtrack(1,[],0)
    return result
k, n = map(int,input().split())
res = combinationSumIII(k,n)
print(*res)

"""
| Aspect               | Answer                                                                                                                                                                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Pruning**                                                                                                                                                                                                                                |
| **Time Complexity**  | **O(C(9, k) × k)** – At most all combinations of choosing `k` numbers from `1` to `9` are explored, and copying each valid combination takes **O(k)**. Since the search space is bounded (`9` numbers), this is effectively constant for the given constraints. |
| **Space Complexity** | **O(k)** – The recursion stack and current `path` store at most `k` numbers (excluding the output list).                                                                                                                                                        |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. The search space is fixed to the numbers `1` through `9`, and pruning (`if total + i > n: break`) avoids unnecessary exploration.                                                                                        |

"""