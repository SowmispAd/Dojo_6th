def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    left, right = 0.0, 1.0

    while True:
        mid = (left + right) / 2
        count = 0
        max_num = 0
        max_den = 1
        j = 1
        for i in range(n):
            while j < n and arr[i] > mid * arr[j]:
                j += 1
            if j == n:
                break
            count += n - j
            if max_num * arr[j] < max_den * arr[i]:
                max_num = arr[i]
                max_den = arr[j]
        if count == k:
            return [max_num, max_den]
        elif count < k:
            left = mid
        else:
            right = mid


arr = list(map(int, input().split()))
k = int(input())

print(kthSmallestPrimeFraction(arr, k))