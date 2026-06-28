def getMaximumGold(grid):
    m,n = len(grid),len(grid[0])
    def dfc(r,c):
        if r<0 or r>=m or c<0 or c>=n or grid[r][c] ==0:
            return 0
        gold = grid[r][c]
        grid[r][c] = 0
        best = max(
            dfc(r+1,c),
            dfc(r-1,c),
            dfc(r,c+1),
            dfc(r,c-1)
        )
        grid[r][c] = gold
        return gold + best
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]!=0:
                ans = max(ans,dfc(i,j))
    return ans

# -------- INPUT PART --------
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the grid row by row:")
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# -------- OUTPUT --------
ans = getMaximumGold(grid)
print("Maximum gold collected:", ans)


"""
| Aspect               | Answer                                                                                                                                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) with Grid Marking (Visited in-place)**                                                                                                                                                                                               |
| **Time Complexity**  | **O(4ᴷ)** worst case – where `K` is number of non-zero cells. From each cell, DFS explores up to 4 directions, leading to exponential exploration in worst case.                                                                                          |
| **Space Complexity** | **O(K)** – Recursion stack depth can go up to the number of cells in the current path.                                                                                                                                                                    |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Since all possible paths must be explored to maximize collected gold, the problem inherently requires exponential search. The in-place marking avoids extra space, making it efficient within optimal constraints. |

"""