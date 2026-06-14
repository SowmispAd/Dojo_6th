arr = list(map(str,input().split()))
def maxLengthOfUniqueStr(arr):
    def is_Unique(s):
        return len(s) == len(set(s))
    res = 0
    def backtrack (index,curr):
        nonlocal res
        if not is_Unique(curr):
            return 
        if len(curr)>res:
            res = len(curr)
        for i in range(index,len(arr)):
            backtrack(i+1,curr+arr[i])
    backtrack(0,"")
    return res
print(maxLengthOfUniqueStr(arr))