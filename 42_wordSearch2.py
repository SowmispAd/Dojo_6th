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


"""
| Aspect               | Answer                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Trie (Prefix Tree) + Backtracking (DFS)**                                                                                                                                                                                                                                                              |
| **Time Complexity**  | **O(W × L + m × n × 4 × 3^(L−1))** – Building the Trie takes **O(W × L)** (`W` = number of words, `L` = maximum word length). DFS starts from each of the `m × n` cells, exploring at most `4 × 3^(L−1)` paths (4 choices initially, then at most 3 thereafter due to not revisiting the previous cell). |
| **Space Complexity** | **O(W × L + L)** – **O(W × L)** for the Trie and **O(L)** for the recursion stack (excluding the output list).                                                                                                                                                                                           |
| **Is it Optimal?**   | **Yes.** This is the optimal approach. Using a Trie prunes invalid search paths early, making it significantly faster than searching each word independently with DFS.                                                                                                                                   |

"""