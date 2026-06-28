def restoreIPAddress(s):
    result = []
    def valid(part):
        if not part or len(part) > 3:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        return int(part) <= 255
    def backtrack(index, path):
        if len(path) == 4:
            if len(s) == index:
                result.append(".".join(path))
                return
            
        for length in range(1,4):
            if index + length >len(s):
                break
            part = s[index:index+length]
            if valid(part):
                backtrack(index+length,path+[part])
    backtrack(0,[])
    return result 
s = input()
print(restoreIPAddress(s))

"""
| Aspect               | Answer                                                                                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Backtracking (DFS) + Recursive Partitioning**                                                                                                                                                             |
| **Time Complexity**  | **O(3⁴) = O(1)** (At most 3 choices for each of the 4 segments, so a maximum of 81 recursive states. Since an IP address has exactly 4 parts, this is constant.)                                            |
| **Space Complexity** | **O(1)** (Recursion depth is at most 4, excluding the output list.)                                                                                                                                         |
| **Is it Optimal?**   | **Yes.** This is the optimal approach. Since every valid partition must be explored and the search space is bounded by a constant (maximum string length is 12), no asymptotically faster algorithm exists. |

"""