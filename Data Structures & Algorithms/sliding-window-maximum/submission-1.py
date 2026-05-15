class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        for i in range(k):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])

        res = [stack[0]]
        l, r = 0, k
        while r < len(nums):
            if nums[l] == stack[0]:
                stack.popleft()
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])
            res.append(stack[0])
            l += 1
            r += 1
        return res