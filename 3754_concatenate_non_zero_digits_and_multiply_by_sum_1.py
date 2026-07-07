class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        for digit in str(n):
            if digit != '0':
                x += digit
        if x == "":
            x = 0
        else:
            x = int(x)
        digit_sum = 0
        for digit in str(x):
            digit_sum += int(digit)
        return x * digit_sum