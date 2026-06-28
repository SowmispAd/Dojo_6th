arr = list(map(int,input().split()))
stack = []
for x in arr:
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
Summary
Approach: Stack (simulation of collisions)
Time Complexity: O(n)
Space Complexity: O(n)

"""