def nxtGreaterElement(nums1,num2):
    nge = {}
    stack = []
    for num in num2:
        while stack and stack[-1]<num:
            nge[stack.pop()] = num
        stack.append(num)
    while stack:
        nge[stack.pop()]= -1
    return [nge[num] for num in nums1]
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
res = nxtGreaterElement(num1,num2)
print(*res)
