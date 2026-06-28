def wordbreak(s,wordDict):
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for w in wordDict:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break

    return dp[-1]
s = input()
wordDict = list(map(str,input().split()))
print(wordbreak(s,wordDict))

"""
| Aspect               | Answer                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Dynamic Programming (Bottom-Up Tabulation)**                                                                                                                                                                                             |
| **Time Complexity**  | **O(n × m × L)** – `n` = length of `s`, `m` = number of words in `wordDict`, `L` = average/max word length. For each position, every word may be checked and compared.                                                                     |
| **Space Complexity** | **O(n)** – The `dp` array stores `n + 1` boolean values.                                                                                                                                                                                   |
| **Is it Optimal?**   | **Yes, for this DP approach.** It is the standard optimal solution. In practice, using a **Hash Set** with maximum word length optimization or a **Trie + DP** can reduce constant factors, but the asymptotic complexity remains similar. |

"""