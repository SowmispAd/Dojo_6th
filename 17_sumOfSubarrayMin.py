def sumSubarrayMin(arr):
    n = len(arr)
    min_sum = 0

    def backtrack(start, end, curr_min):
        nonlocal min_sum

        if end == n:
            return

        curr_min = min(curr_min, arr[end])
        min_sum += curr_min

        backtrack(start, end + 1, curr_min)

    def generate(start):
        if start == n:
            return

        backtrack(start, start, float('inf'))
        generate(start + 1)

    generate(0)
    return min_sum

arr = list(map(int, input().split()))
print(sumSubarrayMin(arr))