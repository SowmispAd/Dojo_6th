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

"""
| Aspect               | Answer                                                                                                                                                            |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Monotonic Increasing Stack**                                                                                                                                    |
| **Time Complexity**  | **O(n)** – Each bar is pushed onto and popped from the stack at most once.                                                                                        |
| **Space Complexity** | **O(n)** – The stack can store up to `n` indices in the worst case.                                                                                               |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every bar must be processed at least once, and the monotonic stack computes the largest rectangle in a single linear pass. |

"""