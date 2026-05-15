class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(visited, i, j, curr):
            c = word[curr]
            if curr == len(word)-1 and board[i][j] == c:
                return True 
            if curr == len(word) or board[i][j] != c:
                return False
            visited.add((i,j))
            curr += 1
            backtrack_res = False
            if 0 <= i - 1 and (i - 1, j) not in visited:
                backtrack_res = backtrack_res or backtrack(visited, i-1, j, curr)
            if i + 1 < len(board) and (i + 1, j) not in visited:
                backtrack_res = backtrack_res or backtrack(visited, i+1, j, curr)
            if 0 <= j - 1 and (i, j-1) not in visited:
                backtrack_res = backtrack_res or backtrack(visited, i, j-1, curr)
            if j + 1 < len(board[0]) and (i, j+1) not in visited:
                backtrack_res = backtrack_res or backtrack(visited, i, j+1, curr)
            visited.remove((i, j))
            return backtrack_res
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c == word[0]:
                    if backtrack(set(), i, j, 0):
                        return True
        return False