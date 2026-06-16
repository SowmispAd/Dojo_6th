arr = list(map(int,input().split()))
stack = []
for x in arr:
    while stack and x<0 and stack[-1] > 0:
        if abs(stack[-1]) < abs(x):
            stack.pop()
            continue
        elif stack[-1] == -x:
            stack.pop()
        break
    else:
        stack.append(x)
print(*stack)