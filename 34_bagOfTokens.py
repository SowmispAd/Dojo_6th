def bagOfTokens(tokens,power):
    tokens.sort()
    n = len(tokens)
    left = 0
    right = n - 1
    score = 0
    max_score = 0
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score,score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score
tokens = list(map(int,input().split()))
power = int(input())
print(bagOfTokens(tokens,power))

"""
| Aspect               | Answer                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Greedy + Two Pointers**                                                                                                                                                                                                                  |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and the two-pointer traversal processes each token at most once (**O(n)**). Overall: **O(n log n)**.                                                                                        |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                                                    |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Sorting is required to greedily spend the smallest token for score and, when necessary, regain power using the largest token. After sorting, a single two-pointer pass achieves the optimal result. |

"""