class Solution:
    def reverse(self, x: int) -> int:
        upper_limit = str((2 ** 31) - 1)
        lower_limit = str((-2 ** 31))
        str_x = list(str(abs(x)))[::-1]
        
        if (len(str_x) > 10):
            return 0
        elif (len(str_x) == 10):
            if (x > 0):
                for i in range(10):
                    if (str_x[i] > list(upper_limit)[i]):
                        return 0
                    elif (str_x[i] < list(upper_limit)[i]):
                        return int(''.join(str_x))
            elif (x < 0):
                for i in range(10):
                    if (str_x[i] > list(lower_limit)[i+1]):
                        return 0
                    elif (str_x[i] < list(lower_limit)[i+1]):
                        return int(''.join(["-"] + str_x))
        else:
            if (x > 0):
                return int(''.join(str_x))
            return int(''.join(["-"] + str_x))              