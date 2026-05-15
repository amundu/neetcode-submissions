class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_1 = [0] * 26 
        counter_2 = [0] * 26

        for i in range(len(s)):
            counter_1[ord(s[i])-ord('a')] += 1
            counter_2[ord(t[i])-ord('a')] += 1

        return counter_1 == counter_2