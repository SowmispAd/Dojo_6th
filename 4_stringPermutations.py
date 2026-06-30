"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

"""

from collections import Counter

s1,s2 = input().split()
def checkInclusion(s1,s2):
    n,m = len(s1),len(s2)
    if n>m:
        return False
    need = Counter(s1)
    window = Counter(s2[:n])
    if need==window:
        return True
    for i in range (n,m):
        window[s2[i]] += 1
        window[s2[i-n]] -=1
        if window[s2[i-n]] == 0:
            del window[s2[i-n]]
        if window == need:
            return True
    return False
print (checkInclusion(s1,s2))


"""
| Aspect               | Answer                                     |
| -------------------- | ------------------------------------------ |
| **Approach**         | Fixed Sliding Window + HashMap (`Counter`) |
| **Time Complexity**  | **O(m)**, where `m = len(s2)`              |
| **Space Complexity** | **O(1)**                                   |
| **Optimized?**       | **Yes**                                    |

"""
    