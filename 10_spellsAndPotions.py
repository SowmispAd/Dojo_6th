from typing import List

def successfulPairs(spells,potions,success):
    potions.sort()
    m = len(potions)
    result = []
    for spell in spells:
        min_potion = (success+spell-1)//spell
        left = 0
        right = m - 1
        first_valid = m
        while left<=right:
            mid = (left+right)//2
            if potions[mid] >= min_potion:
                first_valid = mid
                right = mid - 1
            else:
                left = mid + 1
        result.append(m - first_valid)
    return result

spells = list(map(int,input().split()))
potions = list(map(int,input().split()))
success = int(input())
result = successfulPairs(spells,potions,success)
print(*result)