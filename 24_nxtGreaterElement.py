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

"""
| Aspect               | Answer                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Monotonic Decreasing Stack + Hash Map**                                                                                                                                                                     |
| **Time Complexity**  | **O(n + m)** – `n` = length of `nums1`, `m` = length of `nums2`. Each element in `nums2` is pushed and popped from the stack at most once (**O(m)**), and constructing the result for `nums1` takes **O(n)**. |
| **Space Complexity** | **O(m)** – The stack and hash map together can store up to all elements of `nums2`.                                                                                                                           |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every element in `nums2` must be processed at least once, so **O(n + m)** time and **O(m)** auxiliary space are optimal.                                               |

"""