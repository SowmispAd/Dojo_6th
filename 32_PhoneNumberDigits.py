digits = input()
def letterCombinations(digits):
    if not digits:
        return []
    phone = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : "pqrs",
        '8' : "tuv",
        '9' : 'wxyz'
    }
    res = []
    def backtrack(index,path):
        if index== len(digits):
            res.append(path)
            return
        for ch in phone[digits[index]]:
            backtrack(index+1,path+ch)
    backtrack(0,"")
    return res
result = letterCombinations(digits)
print(*result)

"""
| Aspect               | Answer                                                                                                                                                                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS)**                                                                                                                                                                                                                                |
| **Time Complexity**  | **O(4ⁿ × n)** – Let `n` be the number of digits. Each digit can map to at most **4** letters (digits `7` and `9`), resulting in up to **4ⁿ** combinations. Constructing each combination takes **O(n)**.                                              |
| **Space Complexity** | **O(n)** auxiliary – The recursion stack depth is **O(n)** (excluding the output list).                                                                                                                                                               |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all possible letter combinations, the output size itself is **Θ(4ⁿ × n)** in the worst case. Any algorithm must take at least this much time, making the backtracking solution asymptotically optimal. |

"""