skill = list(map(int,input().split()))
skill.sort()
left = 0
right = len(skill) - 1
total = 0
target = skill[left] + skill[right]
while left<right:
    if skill[left]+skill[right] != target:
        total = (-1)
        break
    total += skill[left]*skill[right]
    left += 1
    right -= 1
print (total)

"""
| Aspect               | Answer                                                                                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach**         | Sort the array, then use **two pointers** to pair the smallest and largest skills. Check if every pair has the same sum; if yes, add their product to the total chemistry. |
| **Algorithm**        | Sorting + Two Pointers                                                                                                                                                     |
| **Time Complexity**  | **O(n log n)** (sorting dominates)                                                                                                                                         |
| **Space Complexity** | **O(1)** extra space *(algorithmically; Python's `sort()` may use `O(n)` auxiliary space)*                                                                                 |
| **Optimized?**       | **Yes.** This is an efficient and commonly accepted solution. A HashMap approach can achieve **O(n)** time but requires **O(n)** extra space.                              |


"""