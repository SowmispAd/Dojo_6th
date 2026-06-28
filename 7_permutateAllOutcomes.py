def permutate(nums):
    nums.sort()
    res = []
    used = [False]*len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return 
        for i in range (len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res
nums = list(map(int,input().split()))
res = permutate(nums)
print(*res)

"""
| Aspect               | Answer                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) with Used Array (Permutation Generation)**                                                                                 |
| **Time Complexity**  | **O(n × n!)** – There are `n!` permutations, and copying each permutation into `res` takes **O(n)**.                                            |
| **Space Complexity** | **O(n)** auxiliary – Recursion depth + `used` array both take **O(n)** space (excluding output list).                                           |
| **Is it Optimal?**   | **Yes.** This is the optimal approach. Since the output itself contains `n!` permutations, any algorithm must take at least **O(n × n!)** time. |

"""