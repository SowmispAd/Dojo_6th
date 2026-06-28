def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[1+i]:
        i-= 1
    if i >= 0 :
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right -= 1


nums = list(map(int,input().split()))
nextPermutation(nums)
print(nums)

"""
| Aspect               | Analysis                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Greedy + Two Pointers** (find pivot, swap with next larger element, reverse suffix)                                  |
| **Time Complexity**  | **O(n)**                                                                                                               |
| **Space Complexity** | **O(1)** (in-place)                                                                                                    |
| **Optimal?**         | **Yes**. This is the optimal algorithm since every element may need to be inspected, giving a lower bound of **O(n)**. |

"""