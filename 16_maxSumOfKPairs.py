def maxOperations(nums,k):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0
    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            right -= 1
            left += 1
            count += 1
        elif total<k:
            left += 1
        else:
            right -= 1
    return count

"""
Summary
Approach: Sorting + Two Pointers
Time Complexity: O(n log n)
Space Complexity:
O(1) auxiliary (algorithmic, excluding sort)
O(n) worst-case due to Python's list.sort() implementation (Timsort)

"""