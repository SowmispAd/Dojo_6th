class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board,words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
    rows, cols = len(board), len(board[0])
    res = set()
    def dfs(r,c,node):
        if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]=="#"):
            return
        ch = board[r][c]
        if ch not in node.children:
            return
        node = node.children[ch]
        if node.word:
            res.add(node.word)
        board[r][c] = "#"
        dfs(r+1,c,node)
        dfs(r-1,c,node)
        dfs(r,c+1,node)
        dfs(r,c-1,node)
        board[r][c] = ch
    for r in range(rows):
        for c in range(cols):
            dfs(r,c,root)
    return list(res)
m, n = map(int, input().split())

board = []
for _ in range(m):
    board.append(input().split())

k = int(input())
words = input().split()

print(findWords(board, words))
