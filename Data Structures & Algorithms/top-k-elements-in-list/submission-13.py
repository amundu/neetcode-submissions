class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # n: freq
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, freq in counter.items():
            buckets[freq].append(n)
        
        output = []
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                output.append(n)
                k -= 1
                if k == 0:
                    return output
