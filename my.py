from functools import reduce
from operator import mul
from re import sub
from sys import set_int_max_str_digits
set_int_max_str_digits(100000)

class Solution:
    def abbreviateProduct(self,l,r):
        s=str(reduce(mul,range(l,r+1)))
        a=sub(r'0+$','',s)
        l=str(len(s)-len(a))
        k=f'e{l}'
        return a+k if len(a)<11 else a[0:5]+'...'+a[-5:]+k

S=Solution()

print(S.abbreviateProduct(44,9556))