def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    def backtrack(start, path):
        if start == len(s):
            return result.append(path[:])
        for end in range(start+1, len(s)+1):
            if is_palindrome(s[start:end]):
                backtrack(end,path+[s[start:end]])


    result = []
    backtrack(0,[])
    return result
s = input()
res = partition(s)
for i in res:
    print(*i)

"""
| Aspect               | Answer                                                                                                                                                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Palindrome Checking**                                                                                                                                                                                                                                           |
| **Time Complexity**  | **O(n × 2ⁿ)** – There are up to **2ⁿ** possible partitions, and each palindrome check (`sub == sub[::-1]`) takes **O(n)** in the worst case.                                                                                                                                           |
| **Space Complexity** | **O(n)** auxiliary – Recursion stack depth and current partition path require **O(n)** space (excluding the output list).                                                                                                                                                              |
| **Is it Optimal?**   | **No.** A more optimized solution precomputes all palindrome substrings using **Dynamic Programming** in **O(n²)** time and then performs backtracking. This reduces repeated palindrome checks, giving an overall complexity of **O(n² + n × 2ⁿ)** while using **O(n²)** extra space. |

"""