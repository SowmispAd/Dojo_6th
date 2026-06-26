def maxValue(n,index,maxsum):
    def calc(peak,length):
        if peak > length:
            small = peak - length
            return (peak -1 + small ) *length // 2
        else:
            return (peak - 1) * peak // 2 + (length - (peak - 1))
    def valid(x):
        left = calc(x,index)
        right = calc(x,n - index - 1)
        total = left + right + x
        return total <= maxsum
    lo, hi = 1, maxsum
    while lo <= hi:
        mid = (lo + hi) // 2
        if valid(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

n, index, maxSum = map(int,input("Enter n, index, maxSum : ").split())
print(maxValue(n,index,maxSum))