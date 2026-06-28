def movingStonesUntilConsecutiveII(stones):
    stones.sort()
    n = len(stones)
    max_moves = max(stones[n-1]-stones[1]-(n-2),stones[n-2]-stones[0]-(n-2))
    min_moves = n
    left = 0
    for right in range(n):
        while stones[right] - stones[left] + 1 > n:
            left += 1
        already = right - left + 1
        if already == n - 1 and stones[right] - stones[left] + 1 == n - 1:
            min_moves = min(min_moves,2)
        else:
            min_moves = min(min_moves,n-already)
    return [min_moves,max_moves]
stones = list(map(int,input().split()))
print(*movingStonesUntilConsecutiveII(stones))

"""
| Aspect               | Answer                                                                                                                                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Sliding Window (for minimum moves) + Greedy Calculation (for maximum moves)**                                                                                                                                           |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and the sliding window traverses the array once (**O(n)**). Overall: **O(n log n)**.                                                                                                 |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                                             |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Sorting is necessary to determine stone positions, and the sliding window computes the minimum moves in linear time while the maximum moves are obtained greedily in **O(1)** after sorting. |

"""