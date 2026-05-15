class Node:
    def __init__(self):
        self.children = {}
        self.is_complete = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_complete = True

    def search(self, word: str) -> bool:
        def dfs(i: int, root: Node) -> bool:
            if i == len(word): return root.is_complete 
            c = word[i]
            if c == '.':
                for child in root.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            if c not in root.children:
                return False
            return dfs(i+1, root.children[c])
        return dfs(0, self.root)

