def canCompleteCircuit(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
gas = list(map(int,input().split()))
cost = list(map(int,input().split()))
print(canCompleteCircuit(gas,cost))

"""
| Aspect               | Answer                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Greedy + Single Pass**                                                                                                                      |
| **Time Complexity**  | **O(n)** – One pass to compute `sum(gas)` and `sum(cost)`, and one pass to find the valid starting station. Overall: **O(n)**.                |
| **Space Complexity** | **O(1)** – Uses only a constant amount of extra space.                                                                                        |
| **Is it Optimal?**   | **Yes.** Every gas station must be visited at least once to determine feasibility, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""