def friendRequests(ages):
    ages.sort()
    n = len(ages)
    left = 0
    right = 0
    ans = 0
    for i in range(n):
        if ages[i] < 15:
            continue
        while ages[left] <= ages[i] * 0.5 + 7:
            left += 1
        while right + 1 < n and ages[right + 1] <= ages[i]:
            right += 1
        ans += right -  left
    return ans
ages = list(map(int,input().split()))
print(friendRequests(ages))

"""
| Aspect               | Answer                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sorting + Two Pointers (Sliding Window)**                                                                                                                                                     |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and the two pointers (`left` and `right`) each traverse the array at most once (**O(n)**). Overall: **O(n log n)**.                              |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                         |
| **Is it Optimal?**   | **Yes.** This is an optimal solution. Any solution must account for ordering, and sorting dominates the complexity, resulting in the optimal **O(n log n)** time with **O(1)** auxiliary space. |

"""