class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        res = []
        for i, n in enumerate(nums):
            if q and q[0][0] < i-k+1:
                q.popleft()
            while q and q[-1][1] < n:
                q.pop()
            q.append((i,n))
            if i >= k-1:
                res.append(q[0][1])
        return res
                