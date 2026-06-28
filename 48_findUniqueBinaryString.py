def findDifferentBinaryString(nums):
    res = []
    for i in range(len(nums)):
        if nums[i][i] == '0':
            res.append('1')
        else:
            res.append('0')
    return "".join(res)
nums = list(map(str,input().split()))
print(findDifferentBinaryString(nums))

"""
| Metric               | Value                                            |
| -------------------- | ------------------------------------------------ |
| **Approach**         | Cantor's Diagonalization (Diagonal Construction) |
| **Time Complexity**  | **O(n)**                                         |
| **Space Complexity** | **O(n)**                                         |
| **Optimal?**         | **Yes**                                          |


"""