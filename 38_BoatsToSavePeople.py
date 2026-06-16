def countBoats(people, w):
    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= w:
            left += 1
        right -= 1
        count += 1
    return boats
people = list(map(int,input().split()))
w = int(input())
print(countBoats(people,w))