def sumSubarrayMin(arr):
    mod = 10**9+7
    n = len(arr)
    left = [0] * n
    right = [0] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i+1
        stack.append(i)
    stack = []
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)
    ans = 0
    for i in range(n):
        ans = (ans + arr[i]*left[i]*right[i])%mod
    return ans


arr = list(map(int, input().split()))
print(sumSubarrayMin(arr))

"""
| Aspect               | Answer                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Monotonic Increasing Stack + Contribution Technique** (computing Previous Less Element and Next Less-or-Equal Element)                                           |
| **Time Complexity**  | **O(n)** – Each element is pushed onto and popped from the stack at most once in each traversal, followed by one linear pass to compute the answer.                |
| **Space Complexity** | **O(n)** – Uses two arrays (`left`, `right`) and a stack, each of size at most `n`.                                                                                |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every element must be processed at least once, and the monotonic stack computes each element's contribution in linear time. |

"""