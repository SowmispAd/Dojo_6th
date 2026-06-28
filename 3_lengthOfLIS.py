#Longest Increasing Subsequence

def lengthOfLIS(nums):
    lis = []
    for num in nums:
        l,r = 0,len(lis)
        while l<r:
            mid = (l+r)//2
            if lis[mid] <num:
                l = mid+1
            else:
                r = mid
        if l == len(lis):
            lis.append(num)
        else:
            lis[l] = num
    return len(lis)
nums = list(map(int,input().split()))
print(lengthOfLIS(nums))

"""
| Aspect               | Answer                                    |
| -------------------- | ----------------------------------------- |
| **Approach**         | Binary Search + Greedy (Patience Sorting) |
| **Time Complexity**  | **O(n log n)**                            |
| **Space Complexity** | **O(n)**                                  |
| **Optimized?**       | **Yes** (Optimal solution)                |

"""