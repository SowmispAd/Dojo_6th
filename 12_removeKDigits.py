def removeKDigits(num,k):
    stack = []
    for digit in num:
        while stack and k>0 and stack[-1]>digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    stack = stack[:-k] if k>0 else stack
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
num = input()
k = int(input())
print(removeKDigits(num,k))  


"""
| Aspect               | Analysis                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Monotonic increasing stack (Greedy + Stack)**                                                                          |
| **Time Complexity**  | **O(n)** (each digit is pushed and popped at most once)                                                                  |
| **Space Complexity** | **O(n)** (stack storage for digits)                                                                                      |
| **Optimal?**         | **Yes**. This is the standard optimal solution for removing k digits problem                                             |
| **Key Idea**         | Maintain increasing stack so larger digits are removed early to minimize number; leftover `k` handled by trimming suffix |
| **Correctness**      | Correct, handles leading zeros and leftover removals properly                                                            |

"""
