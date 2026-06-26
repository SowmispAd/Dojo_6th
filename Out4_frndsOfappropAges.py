def friendRequests(ages):
    ages.sort()
    n = len(ages)
    left = 0
    right = 0
    ans = 0
    for i in range(n):
        if ages[i] < 15:
            continue
        while ages[left] <= ages[i] * 0.5 + 7:
            left += 1
        while right + 1 < n and ages[right + 1] <= ages[i]:
            right += 1
        ans += right -  left
    return ans
ages = list(map(int,input().split()))
print(friendRequests(ages))

    