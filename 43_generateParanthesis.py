def generateParenthesis(n):
    ans = []
    def solve(s,open,close):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if open < n:
            solve(s+"(",open+1,close)
        if close < open:
            solve(s+")",open,close+1)
    solve("",0,0)
    return ans
n = int(input())
print(generateParenthesis(n))

"""
| Aspect               | Answer                                                                                                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS)**                                                                                                                                                                                                                  |
| **Time Complexity**  | **O(Cₙ × n)** – `Cₙ` is the **n-th Catalan number** (approximately `4ⁿ / (n^(3/2)√π)`). There are `Cₙ` valid parenthesis strings, and constructing each string takes **O(n)**.                                                          |
| **Space Complexity** | **O(n)** auxiliary – Maximum recursion depth is `2n` (i.e., **O(n)**), excluding the output list.                                                                                                                                       |
| **Is it Optimal?**   | **Yes.** Since the problem requires generating all valid parenthesis combinations, the output size itself is **Θ(Cₙ × n)**. Any algorithm must spend at least this much time, making this backtracking solution asymptotically optimal. |

"""