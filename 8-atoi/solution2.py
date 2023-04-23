import re

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s)
        if match:
            # extract the matched digits and convert to integer
            num = int(match.group(1))
            
            # clamp to the 32-bit signed integer range
            num = max(min(num, 2**31 - 1), -2**31)
            
            return num
        
        else:
            return 0
