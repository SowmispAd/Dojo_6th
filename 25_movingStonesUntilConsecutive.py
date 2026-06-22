def movingStonesUntilConsecutiveII(stones):
    stones.sort()
    n = len(stones)
    max_moves = max(stones[n-1]-stones[1]-(n-2),stones[n-2]-stones[0]-(n-2))
    min_moves = n
    left = 0
    for right in range(n):
        while stones[right] - stones[left] + 1 > n:
            left += 1
        already = right - left + 1
        if already == n - 1 and stones[right] - stones[left] + 1 == n - 1:
            min_moves = min(min_moves,2)
        else:
            min_moves = min(min_moves,n-already)
    return [min_moves,max_moves]
stones = list(map(int,input().split()))
print(*movingStonesUntilConsecutiveII(stones))