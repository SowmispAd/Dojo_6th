def maxConsecutiveAnswers(answerKey,k):
    n = len(answerKey)
    def max_length(target):
        left = 0 
        changes = 0
        max_changes = 0
        for right in range (n):
            if answerKey[right] != target:
                changes += 1
            while changes > k:
                if answerKey[left] != target:
                    changes -= 1
                left += 1
            max_changes = max(max_changes,right - left+1)
        return max_changes
    return max(max_length('T'),max_length('F'))
answerKey = input()
k = int(input())
print(maxConsecutiveAnswers(answerKey,k))

"""
| Aspect               | Answer                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Sliding Window (run twice: once treating `'T'` as the target and once treating `'F'` as the target)**                                           |
| **Time Complexity**  | **O(n)** – The sliding window traverses the string once for `'T'` and once for `'F'`, resulting in **O(2n) = O(n)**.                              |
| **Space Complexity** | **O(1)** – Uses only a constant number of variables.                                                                                              |
| **Is it Optimal?**   | **Yes.** This is the optimal solution. Every character must be examined at least once, so **O(n)** time and **O(1)** auxiliary space are optimal. |

"""