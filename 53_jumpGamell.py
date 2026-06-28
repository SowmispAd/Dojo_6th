def jump(nums):
    jumps = 0
    curr_end = 0
    farthest = 0
    for i in range(len(nums)-1):
        farthest = max(farthest,i+nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
    return jumps
nums = list(map(int,input().split())) 
print(jump(nums))

"""
| Aspect               | Answer                                                                                                                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Greedy + Sliding Window (Range Expansion)**                                                                                                                                            |
| **Time Complexity**  | **O(n)** – Each index is visited exactly once while maintaining the farthest reachable position in the current jump range.                                                               |
| **Space Complexity** | **O(1)** – Uses only a constant amount of extra space.                                                                                                                                   |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every element must be examined at least once to determine the minimum number of jumps, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""