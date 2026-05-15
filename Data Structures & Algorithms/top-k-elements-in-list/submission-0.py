class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        occurrences = [[] for _ in range(len(nums)+1)]
        for e, i in counter.items():
            occurrences[i].append(e)
        
        top_elements = []
        for i in range(len(occurrences)-1, 0, -1):
            if occurrences[i]:
                for n in occurrences[i]:
                    top_elements.append(n)
                    k -= 1
                    if k == 0:
                        break
            if k == 0:
                break
        return top_elements