def solveNQueens(n):
        board = [["."]*n for i in range(n)]
        ans = []
        def isSafe(row,col):
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i, j = row-1,col-1
            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False

                i -= 1
                j -= 1
            i,j = row-1, col+1
            while i>=0 and j<n:
                if board[i][j] =="Q":
                    return False
                i-=1
                j+=1
            return True
        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return 
            for col in range (n):
                if isSafe(row,col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        backtrack(0)
        return ans
            
            
            
n = int(input())
res = solveNQueens(n)
for i in res:
    print(*i)
"""
| Aspect               | Answer                                                                                                                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Safety Checking**                                                                                                                                                                                                                                      |
| **Time Complexity**  | **O(n! × n)** – In the worst case, backtracking explores up to `n!` queen placements. Each `isSafe()` check takes **O(n)** (row, column, and diagonals).                                                                                                                      |
| **Space Complexity** | **O(n²)** – The chessboard requires **O(n²)** space, and the recursion stack uses **O(n)** (excluding the output list).                                                                                                                                                       |
| **Is it Optimal?**   | **No.** A more optimized solution uses **three hash sets (or bitmasks)** to track occupied columns and diagonals, reducing each safety check to **O(1)**. This improves the overall time complexity to **O(n!)** while using **O(n)** auxiliary space (excluding the output). |

"""