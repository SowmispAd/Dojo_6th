def largestReactangleHistogram(heights):
    n = len(heights)
    stack = []
    max_area = 0
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            if stack:
                width = i - stack[-1] -1
            else:
                width = i
            area = h * width
            if area > max_area:
                max_area = area
        stack.append(i)
    while stack:
        h = heights[stack.pop()]
        if stack:
            width = n - stack[-1] - 1
        else:
            width = n
        area = h * width
        if area > max_area:
            max_area = area
    return max_area
heights = list(map(int,input().split()))
print(largestReactangleHistogram(heights))