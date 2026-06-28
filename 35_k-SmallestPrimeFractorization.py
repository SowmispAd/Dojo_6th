def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    left, right = 0.0, 1.0

    while True:
        mid = (left + right) / 2
        count = 0
        max_num = 0
        max_den = 1
        j = 1
        for i in range(n):
            while j < n and arr[i] > mid * arr[j]:
                j += 1
            if j == n:
                break
            count += n - j
            if max_num * arr[j] < max_den * arr[i]:
                max_num = arr[i]
                max_den = arr[j]
        if count == k:
            return [max_num, max_den]
        elif count < k:
            left = mid
        else:
            right = mid


arr = list(map(int, input().split()))
k = int(input())

print(kthSmallestPrimeFraction(arr, k))

"""
| Aspect               | Answer                                                                                                                                                                                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Binary Search on Answer + Two Pointers**                                                                                                                                                                                                                                                                  |
| **Time Complexity**  | **O(n × log(1/ε))** – Each binary search iteration scans the array once using two pointers (**O(n)**), and the binary search requires **O(log(1/ε))** iterations to achieve the desired precision (`ε`).                                                                                                    |
| **Space Complexity** | **O(1)** – Uses only a constant amount of extra space.                                                                                                                                                                                                                                                      |
| **Is it Optimal?**   | **Yes.** This is one of the optimal solutions. Another optimal approach uses a **Min Heap (Priority Queue)** with **O((n + k) log n)** time and **O(n)** space. Which is better depends on the relative sizes of `n` and `k`; the binary search approach is the standard optimal solution for this problem. |

"""