from typing import List

def successfulPairs(spells,potions,success):
    potions.sort()
    m = len(potions)
    result = []
    for spell in spells:
        min_potion = (success+spell-1)//spell
        left = 0
        right = m - 1
        first_valid = m
        while left<=right:
            mid = (left+right)//2
            if potions[mid] >= min_potion:
                first_valid = mid
                right = mid - 1
            else:
                left = mid + 1
        result.append(m - first_valid)
    return result

spells = list(map(int,input().split()))
potions = list(map(int,input().split()))
success = int(input())
result = successfulPairs(spells,potions,success)
print(*result)

"""
| Aspect               | Answer                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Binary Search**                                                                                                                                                     |
| **Time Complexity**  | **O(m log m + n log m)** – Sorting `potions` takes **O(m log m)**, and for each of the `n` spells, a binary search over `m` potions takes **O(log m)**.                         |
| **Space Complexity** | **O(1)** auxiliary (excluding the output list). Python's built-in `sort()` uses **O(log m)** stack space in the worst case due to Timsort.                                      |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Sorting the potions once and performing binary search for each spell achieves the best possible asymptotic complexity for this approach. |

"""