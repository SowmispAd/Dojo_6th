def threeSumClosest(nums,target):
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]
    for i in range (n-2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - result):
                result = total
            if total == target:
                return target
            elif total < target:
                left += 1
            else:
                right -= 1
    return result
nums = list(map(int,input().split()))

target = int(input())
print(threeSumClosest(nums,target))