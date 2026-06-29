from collections import defaultdict
def totalFruits(fruits):
    left = 0
    count = defaultdict(int)
    max_count = 0
    for right in range(len(fruits)):
        count[fruits[right]] += 1
        while len(count)>2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1 # Don't forget the increment of left
        max_count = max(max_count,right - left + 1)
    return max_count

fruits = list(map(int,input().split()))
print(totalFruits(fruits))

"""
| Aspect               | Answer                                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sliding Window + Hash Map (Frequency Counter)**                                                                                              |
| **Time Complexity**  | **O(n)** – Each element is added to and removed from the sliding window at most once.                                                          |
| **Space Complexity** | **O(1)** – The hash map stores at most **2** fruit types, so the auxiliary space is constant.                                                  |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every fruit must be processed at least once, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""