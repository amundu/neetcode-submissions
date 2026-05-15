class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        for i in range(len(num2)-1, -1, -1):
            subtotal = 0
            for j in range(len(num1)-1, -1, -1):
                subtotal += int(num2[i]) * int(num1[j]) * (10**(len(num1)-1-j))
            print(subtotal)
            total += subtotal * (10**(len(num2)-1-i))
        return str(total)