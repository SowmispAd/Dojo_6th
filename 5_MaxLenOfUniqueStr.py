arr = list(map(str,input().split()))
def maxLengthOfUniqueStr(arr):
    def is_Unique(s):
        return len(s) == len(set(s))
    res = 0
    def backtrack (index,curr):
        nonlocal res
        if not is_Unique(curr):
            return 
        if len(curr)>res:
            res = len(curr)
        for i in range(index,len(arr)):
            backtrack(i+1,curr+arr[i])
    backtrack(0,"")
    return res
print(maxLengthOfUniqueStr(arr))

"""
| Aspect               | Answer                                                                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Pruning using Character Uniqueness Check**                                                                                                                                                                                                   |
| **Time Complexity**  | **O(2ⁿ × L)** – There are up to `2ⁿ` subsets of strings (`n` = number of strings), and checking whether the concatenated string is unique takes **O(L)**, where `L` is the length of the current concatenated string (bounded by 26 for lowercase English letters). |
| **Space Complexity** | **O(n + L)** – **O(n)** recursion stack and **O(L)** for the current concatenated string (excluding the output).                                                                                                                                                    |
| **Is it Optimal?**   | **Yes.** Since all subsets may need to be explored, the worst-case time is exponential. A bitmask-based implementation improves constant factors by replacing repeated uniqueness checks with bitwise operations, but the asymptotic complexity remains **O(2ⁿ)**.  |

"""