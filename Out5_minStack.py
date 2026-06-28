class MinStack:

    def __init__(self):
        
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)
        

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
| Aspect                       | Analysis                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Approach Used**            | **Auxiliary Stack (Monotonic Min Tracking Stack)**                                |
| **Time Complexity (push)**   | **O(1)**                                                                          |
| **Time Complexity (pop)**    | **O(1)**                                                                          |
| **Time Complexity (top)**    | **O(1)**                                                                          |
| **Time Complexity (getMin)** | **O(1)**                                                                          |
| **Space Complexity**         | **O(n)** (two stacks in worst case)                                               |
| **Optimal?**                 | **Yes** (this is the standard optimal solution for MinStack with O(1) operations) |

**Note:** Your implementation is correct and handles duplicates properly using `<=` in `push`.

"""