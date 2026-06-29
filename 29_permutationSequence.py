def getPermutation(n, k):
    nums = [str(i) for i in range(1,n+1)]
    fact = 1
    for i in range(1, n):
        fact *= i
    k -= 1
    ans = []
    while nums:
        index = k // fact                   # Remeber k // fact
        ans.append(nums.pop(index))
        k %= fact # Remeber this
        if not nums:
            break
        fact //= len(nums)
    return "".join(ans)
n,k = map(int,input().split())
print(getPermutation(n,k))

"""
| Aspect               | Answer                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Factorial Number System (Factoradic) + Greedy Selection**                                                                                                                                                                                                                                                                                                                                                 |
| **Time Complexity**  | **O(n²)** – `pop(index)` from a Python list takes **O(n)** in the worst case, and it is performed `n` times.                                                                                                                                                                                                                                                                                                |
| **Space Complexity** | **O(n)** – for the `nums` list and the `ans` list.                                                                                                                                                                                                                                                                                                                                                          |
| **Is it Optimal?**   | **Yes**, for this implementation using Python lists. The factoradic approach is optimal in terms of avoiding generation of all permutations (`O(n!)`). The only overhead is `pop(index)`, making the overall complexity **O(n²)**. Achieving better than **O(n²)** requires more advanced data structures (e.g., Fenwick Tree, Segment Tree, or Balanced BST), which can reduce the time to **O(n log n)**. |

"""