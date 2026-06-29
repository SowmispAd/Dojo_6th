def maxValue(n,index,maxsum):
    def calc(peak,length):
        if peak > length:
            small = peak - length
            return (peak -1 + small ) *length // 2
        else:
            return (peak - 1) * peak // 2 + (length - (peak - 1))
    def valid(x):
        left = calc(x,index)
        right = calc(x,n - index - 1) #make sure u have -1
        total = left + right + x
        return total <= maxsum
    lo, hi = 1, maxsum
    while lo <= hi:
        mid = (lo + hi) // 2 
        if valid(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

n, index, maxSum = map(int,input("Enter n, index, maxSum : ").split())
print(maxValue(n,index,maxSum))

"""
| Aspect               | Answer                                                                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Binary Search on Answer + Mathematical (Arithmetic Series) Calculation**                                                                                                                                                    |
| **Time Complexity**  | **O(log(maxSum))** – Binary search over the possible value range `[1, maxSum]`, with each validity check taking **O(1)**.                                                                                                     |
| **Space Complexity** | **O(1)** – Uses only a constant number of variables.                                                                                                                                                                          |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Since the answer lies within a monotonic range, binary search with constant-time validation achieves the best possible asymptotic complexity of **O(log(maxSum))** and **O(1)** space. |

"""