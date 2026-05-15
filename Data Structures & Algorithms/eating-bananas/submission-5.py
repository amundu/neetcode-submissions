class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles) # min_k, max_k = 1, 4
        res = max_k
        while min_k <= max_k:
            m_k = (max_k + min_k) // 2 # mid k = (4+1)//2 = 2
            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(float(pile)/m_k)
                if temp_h > h:
                    break
            if temp_h <= h:
                res = m_k
                max_k = m_k - 1
            else:
                min_k = m_k + 1
        return res
            