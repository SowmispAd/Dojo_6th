from typing import List
from collections import defaultdict

def beautifulSubsets(nums,k):
    freq = defaultdict(int)
    count = 0
    def backtack(index):
        nonlocal count
        if index == len(nums):
            count += 1
            return
        backtack(index + 1)
        num = nums[index]
        if freq[num - k] == 0 and freq[num + k] == 0:
            freq[num] += 1
            backtack(index + 1)
            freq[num] -= 1
    backtack(0)
    return count - 1
nums = list(map(int,input().split()))
k = int(input())
print(beautifulSubsets(nums,k))