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

"""
| Aspect               | Answer                                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Binary Search on Answer**                                                                                                                                                                                                                          |
| **Time Complexity**  | **O(n × log M)** – `n` = number of piles, `M` = maximum pile size. Each binary search iteration scans all piles (**O(n)**), and there are **O(log M)** iterations.                                                                                   |
| **Space Complexity** | **O(1)** – Uses only a constant amount of extra space.                                                                                                                                                                                               |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. The search space is monotonic (if Koko can finish at speed `k`, she can also finish at any speed `> k`), making binary search on the answer the optimal approach with **O(n log M)** time and **O(1)** space. |

"""