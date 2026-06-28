def minimumRefill(plants,capacityA,capacityB):
    left = 0
    right = len(plants) - 1
    refill = 0
    waterA = capacityA
    waterB = capacityB

    while left < right:
        if waterA < plants[left]:
            refill += 1
            waterA = capacityA
        waterA -= plants[left]

        if waterB < plants[right]:
            refill += 1
            waterB = capacityB
        waterB -= plants[right]

        left += 1
        right -= 1
    if left == right:
        if max(waterA,waterB) < plants[left]:
            refill += 1
    return refill
plants = list(map(int,input().split()))
alice = int(input())
bob = int(input())
print(minimumRefill(plants,alice,bob))

"""
| Aspect               | Answer                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Two Pointers (Alice from left, Bob from right) + Greedy Simulation**                                          |
| **Time Complexity**  | **O(n)** – Each plant is processed exactly once.                                                                |
| **Space Complexity** | **O(1)** – Uses only a few variables regardless of input size.                                                  |
| **Is it Optimal?**   | **Yes.** Every plant must be examined at least once, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""