class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        output = []
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix = output[i]
            output[i] = prefix * postfix
            postfix *= nums[i]
        
        return output


