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