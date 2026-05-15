class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while carry and i >= 0:
            curr = digits[i] + carry
            digits[i] = curr % 10
            carry = curr // 10
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
