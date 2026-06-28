def countBoats(people, w):
    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= w:
            left += 1
        right -= 1
        boats += 1
    return boats
people = list(map(int,input().split()))
w = int(input())
print(countBoats(people,w))

"""
| Aspect               | Answer                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Approach Used**    | **Greedy + Two Pointers**                                                                                                                                                                                          |
| **Time Complexity**  | **O(n log n)** – Sorting takes **O(n log n)**, and the two-pointer traversal takes **O(n)**. Overall: **O(n log n)**.                                                                                              |
| **Space Complexity** | **O(1)** auxiliary (excluding the space used by Python's sorting algorithm). Python's built-in `sort()` uses **O(log n)** stack space in the worst case due to Timsort.                                            |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Sorting is necessary to greedily pair the lightest and heaviest remaining people, yielding the minimum number of boats. After sorting, the two-pointer traversal is linear. |

"""