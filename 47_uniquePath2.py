def uniquePath2(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    dp = [0] * cols
    dp[0] = 1
    for r in range(rows):
        for c in range(cols):
            if obstacleGrid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]
rows, cols = map(int,input().split())
obstacleGrid = [list(map(int,input().split())) for _ in range(rows)]
print(uniquePath2(obstacleGrid))

"""
| Metric               | Value                                       |
| -------------------- | ------------------------------------------- |
| **Approach**         | Dynamic Programming (1D Space-Optimized DP) |
| **Time Complexity**  | **O(m × n)**                                |
| **Space Complexity** | **O(n)**                                    |
| **Optimal?**         | **Yes**                                     |

"""