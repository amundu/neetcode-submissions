class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        for i in range(k):
            while queue and queue[-1][1] < nums[i]:
                queue.pop()
            queue.append((i, nums[i]))
        
        res = [queue[0][1]]

        for i in range(k, len(nums)):
            if queue[0][0] == i - k:
                queue.popleft()
            while queue and queue[-1][1] < nums[i]:
                queue.pop()
            queue.append((i, nums[i]))
            res.append(queue[0][1])
        return res