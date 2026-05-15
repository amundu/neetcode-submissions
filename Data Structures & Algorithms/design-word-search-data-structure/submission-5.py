class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        if not word:
            return True
        curr = self.root
        def dfs(curr, i):
            if i == len(word):
                return False
            c = word[i]
            if c != '.':
                if c not in curr.children:
                    return False
                if i < len(word) -1:
                    return dfs(curr.children[c], i + 1)
                return curr.children[c].is_end_of_word
            else:
                if i == len(word)-1:
                    for child in curr.children.values():
                        if child.is_end_of_word:
                            return True
                    return False
                # backtracking
                for c, node in curr.children.items():
                    if dfs(node, i + 1):
                        return True
                return False
        return dfs(curr, 0)
