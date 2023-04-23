class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # if dividend == 0, result is 0
        if dividend == 0:
            return 0
        # check sign (++ or -- = +)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
       # get the absolut values
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result
