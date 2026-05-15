class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        nums_frequencies = [[] for _ in range(len(nums))]
        for n, frequency in counter.items():
            nums_frequencies[frequency-1].append(n)
        
        res = []
        for i in range(len(nums_frequencies)-1, -1, -1):
            curr = nums_frequencies[i]
            while len(curr) and len(res) != k:
                res.append(curr.pop())
        return res