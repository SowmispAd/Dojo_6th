def countSmaller(nums):
    from bisect import bisect_left,insort
    ans = []
    sorted_arr = []
    for num in reversed(nums):
        idx = bisect_left(sorted_arr,num)
        ans.append(idx)
        insort(sorted_arr,num)
    return ans[::-1]

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    result = countSmaller(nums)
    print(*result)