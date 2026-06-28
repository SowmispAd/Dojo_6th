def exist(board,word):
    rows, cols = len(board), len(board[0])
    path = set()
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!= word[i] or (r,c) in path ):
            return False
        path.add((r,c))
        res = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or 

            dfs(r, c+1, i+1) or
            dfs(r, c-1,i+1)
        )
        path.remove((r,c))
        return res
    for r in range(rows):
        for c in range (cols):
            if dfs(r,c,0): return True

    return False
    
"""
| Aspect               | Answer                                                                                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Visited Set**                                                                                                                                                                        |
| **Time Complexity**  | **O(m × n × 3ᴸ)** – `m × n` possible starting cells, and for each, DFS explores at most **3** directions after the first move (the previous cell cannot be revisited), where `L` is the length of the word. |
| **Space Complexity** | **O(L)** – The recursion stack and the `path` (visited set) can each grow up to the length of the word.                                                                                                     |
| **Is it Optimal?**   | **Yes.** This is the standard optimal solution. In the worst case, all possible paths must be explored, so no asymptotically faster algorithm exists for the general problem.                               |

"""