def minEatingSpeed(piles,h):
    left = 1
    right = max(piles)
    answer = right
    while left<=right :
        mid = (left+right)//2
        hours = 0
        for pile in piles:
            hours += (pile+mid-1)//mid
        if hours<=h:  #Take care it is less than 
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

piles = list(map(int,input().split()))
h = int(input())
print (minEatingSpeed(piles,h))

