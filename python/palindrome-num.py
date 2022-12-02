import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        def pos_i_digit(i: int, n: int):
            reduced = n % (10**i)
            return (reduced - reduced % (10**(i - 1))) // (10 ** (i - 1))

        num_digits = math.floor(math.log10(x)) + 1
        for i in range(num_digits//2 ):
            if pos_i_digit(i+1, x) != pos_i_digit(num_digits - i, x):
                return False
            
        return True
