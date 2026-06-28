def splitString(s):
    def dfs(index, prev, count):
        if index == len(s):
            return count >= 2
        num = 0
        for i in range(index,len(s)):
            num = num * 10 + int(s[i])
            if num == prev - 1:
                if dfs(i+1,num,count+1):
                 return True
            elif num >= prev:
                break
        return False
    first = 0
    for i in range(len(s)-1):
        first = first * 10 + int(s[i])
        if dfs(i+1,first,1):
            return True
    return False
s = input()
print(splitString(s))


"""
| Aspect               | Answer                                                                                                                                                                                                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Recursive Partitioning**                                                                                                                                                                                    |
| **Time Complexity**  | **O(2ⁿ)** (worst case, explores exponentially many possible partitions of the string)                                                                                                                                              |
| **Space Complexity** | **O(n)** (recursion stack depth up to `n`)                                                                                                                                                                                         |
| **Is it Optimal?**   | **Yes.** This is the standard optimal approach for this problem because there is no known polynomial-time algorithm. In the worst case, multiple partition possibilities must be explored, leading to exponential time complexity. |

"""