def numMovesStones(a,b,c):
    a,b,c = sorted([a,b,c])
    gap1 = b - a
    gap2 = c - b
    if c - a == 2:
        return [0,0]
    if gap1 <= 2 or gap2 <= 2:
        min_moves = 1
    else:
        min_moves = 2
    max_moves = c - a - 2
    return [min_moves, max_moves]
a, b, c = map(int,input().split())
print(numMovesStones(a,b,c))

"""
| Aspect               | Answer                                                                                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Greedy + Mathematical Observation**                                                                                                                                                     |
| **Time Complexity**  | **O(1)** – Performs a constant number of comparisons and arithmetic operations.                                                                                                           |
| **Space Complexity** | **O(1)** – Uses only a constant amount of extra space.                                                                                                                                    |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. The answer is derived directly from the relative positions of the three stones using mathematical observations, requiring constant time and space. |

"""