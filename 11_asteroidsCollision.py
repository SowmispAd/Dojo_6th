arr = list(map(int,input().split()))
stack = []
for x in arr:
    alive = True
    while stack and x<0 and stack[-1] > 0:
        if abs(stack[-1]) < abs(x):
            stack.pop()
            continue
        elif stack[-1] == -x:
            stack.pop()
            alive = False

        else:
            alive = False
    if alive:
        stack.append(x)
print(*stack)

"""
| Aspect               | Analysis                                                                                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Stack-based collision simulation (typical “asteroid collision” style problem)**                                                                                            |
| **Time Complexity**  | **O(n)** (each element is pushed/popped at most once)                                                                                                                        |
| **Space Complexity** | **O(n)** (stack storage in worst case)                                                                                                                                       |
| **Optimal?**         | **Yes** for this class of collision problems, since each element must be processed at least once                                                                             |
| **Issues in Code**   | `alive` is used without initialization for each `x`, and logic does not properly handle all collision cases (especially when multiple pops or surviving states are involved) |


"""