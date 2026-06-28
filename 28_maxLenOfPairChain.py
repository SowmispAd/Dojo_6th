import ast
def findLongestChain(pairs):
    pairs.sort(key=lambda x:x[1] )
    count = 0
    prev_end = float("-inf")
    for start,end in pairs:
        if start>prev_end:
            count += 1
            prev_end = end
    return count
pairs = ast.literal_eval(input())
print(findLongestChain(pairs))

"""
Summary

Approach : Greedy (Activity Selection)
Sorting Key : Pair end value
Time Complexity : O(n log n)
Space Complexity : O(1) auxiliary
Optimal? Yes

"""