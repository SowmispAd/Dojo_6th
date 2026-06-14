skill = list(map(int,input().split()))
skill.sort()
left = 0
right = len(skill) - 1
total = 0
target = skill[left] + skill[right]
while left<right:
    if skill[left]+skill[right] != target:
        total = (-1)
        break
    total += skill[left]*skill[right]
    left += 1
    right -= 1
print (total)