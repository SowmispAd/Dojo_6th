
def permutaionsUnique(nums):
    nums.sort()
    res = []
    used = [False]*len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] :
                continue 
            if i >0 and nums[i] == nums[i - 1]  and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res
nums = list(map(int,input().split()))
print(permutaionsUnique(nums))

"""
| Aspect               | Analysis                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Backtracking (DFS) with sorting + used array + duplicate pruning**                                                     |
| **Time Complexity**  | **O(n! × n)** (all unique permutations, each of length n is copied/constructed)                                          |
| **Space Complexity** | **O(n)** auxiliary (recursion stack + `used` array), excluding output                                                    |
| **Optimal?**         | **Yes** for generating all unique permutations. Output size itself is **O(n! × n)**, so this is asymptotically optimal.  |
| **Key Idea**         | Sorting + skipping duplicates using `if i > 0 and nums[i] == nums[i-1] and not used[i-1]` prevents repeated permutations |

"""