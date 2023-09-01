from math import factorial as f
from sys import set_int_max_str_digits as s
from re import sub
s(100000)

class Solution:
    def trailingZeroes(self,n):
        r=sub(r'0+$',lambda e:'&'+e.group(),str(f(n))).split('&')[-1]
        return 0 if '0' not in r else len(r)
    
s=Solution()

print(s.trailingZeroes(1223))