class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]
        for n, freq in counter.items():
            bucket[freq].append(n)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            while bucket[i] and k > 0:
                res.append(bucket[i].pop())
                k -= 1
                if k == 0:
                    return res