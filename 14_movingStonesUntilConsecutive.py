def numMovesStones(a,b,c):
    a,b,c = sorted([a,b,c])
    gap1 = b - a
    gap2 = c - b
    if c - a == 2:
        return [0,0]
    if gap1 <= 2 or gap2 <= 2:
        min_moves = 1
    else:
        min_moves = 2
    max_moves = c - a - 2
    return [min_moves, max_moves]
a, b, c = map(int,input().split())
print(numMovesStones(a,b,c))