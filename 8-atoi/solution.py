class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # check if the next character is '-' or '+'
        if s[0] in ['-', '+']:
            sign = s[0]
            s = s[1:]
        else:
            sign = ''
            
        # read in digits until the next non-digit character or the end of the input
        num_str = ''
        for c in s:
            if c.isdigit():
                num_str += c
            else:
                break
        
        # convert digits to integer and apply sign
        if not num_str:
            return 0
        else:
            num = int(sign + num_str) if sign else int(num_str)
        
        # clamp integer to 32-bit signed integer range
        num = max(-2**31, num)
        num = min(2**31 - 1, num)
        
        return num
    