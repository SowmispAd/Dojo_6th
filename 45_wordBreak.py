def wordbreak(s,wordDict):
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for w in wordDict:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break

    return dp[-1]
s = input()
wordDict = list(map(str,input().split()))
print(wordbreak(s,wordDict))