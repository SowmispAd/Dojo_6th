def subarrayRanges(nums):
    n = len(nums)
    ans = 0
    for i in range(n):
        smallest = nums[i]
        greatest = nums[i]
        for j in range(i,n):
            smallest = min(smallest,nums[j])
            greatest = max(greatest,nums[j])
            ans += greatest - smallest
    return ans
nums = list(map(int,input().split()))
print(subarrayRanges(nums))

"""
| Aspect                       | Details                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| **Approach Used**            | Brute Force (Nested Loops with running minimum and maximum)                              |
| **Time Complexity**          | **O(n²)**                                                                                |
| **Space Complexity**         | **O(1)**                                                                                 |
| **Optimal?**                 | **No**                                                                                   |
| **Optimal Time Complexity**  | **O(n)**                                                                                 |
| **Optimal Space Complexity** | **O(n)**                                                                                 |
| **Optimal Approach**         | Monotonic Stacks (compute each element's contribution as maximum and minimum separately) |

"""