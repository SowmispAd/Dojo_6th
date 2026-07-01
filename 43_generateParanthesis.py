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


| Notation    | Pronounce as                                                             |
| ----------- | ------------------------------------------------------------------------ |
| `O(Cₙ)`     | "Big O of C sub n" or "Big O of the n-th Catalan number"                 |
| `O(Cₙ × n)` | "Big O of C sub n times n" or "Big O of the n-th Catalan number times n" |
| `O(2ⁿ)`     | "Big O of two to the power n"                                            |
| `O(n!)`     | "Big O of n factorial"                                                   |

The n-th Catalan number is
                         Cn ​= (2n)!/ (n+1)!n!    (catalan come in combinometric
________________________                         
| n | Catalan Number Cₙ  |
| - | ----------------- |
| 0 | 1                 |
| 1 | 1                 |
| 2 | 2                 |
| 3 | 5                 |
| 4 | 14                |
| 5 | 42                |
| 6 | 132               |
| 7 | 429               |
________________________|


For coding interviews, it's usually enough to know:

Cₙ is the n-th Catalan number.
It counts the number of valid structures in problems like Generate Parentheses and Unique BSTs.
When a solution generates all such structures, the time complexity is often O(Cₙ × n) because there are Cₙ outputs, each requiring O(n) work.


| Term                           | Meaning                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------- |
| **Catalan Number**             | A sequence that counts certain combinatorial structures.                     |
| **n-th Catalan Number (`Cₙ`)** | The n-th value in the Catalan sequence.                                      |
| **Catalan Sequence**           | The sequence: 1, 1, 2, 5, 14, 42, 132, ...                                   |
| **Combinatorics**              | The branch of mathematics dealing with counting arrangements and structures. |



"""