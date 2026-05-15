class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[-1], cost[-2]
        for i in range(len(cost)-3, -1, -1):
            c = cost[i] + min(a,b)
            a, b = b, c
        return min(a,b)