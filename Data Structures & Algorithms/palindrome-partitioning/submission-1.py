class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        
        def is_palindrome(subs):
            if not subs:
                return False
            l,r = 0, len(subs)-1
            while l < r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1
            return True

        output = []
        path = []
        def dfs(idx):
            if idx == len(s):
                print(path)
                output.append(path[:])
                return
            for i in range(idx+1, len(s)+1):
                subs = s[idx:i]
                if not is_palindrome(subs):
                    continue
                path.append(subs)
                dfs(i)
                path.pop()
        dfs(0)
        return output

            