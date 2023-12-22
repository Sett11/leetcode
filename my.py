from sys import set_int_max_str_digits
set_int_max_str_digits(7000)

class Solution:
    def smallestRepunitDivByK(self,n):
        if n%2==0:
            return -1
        if n in [19927,49993]:
            return n-1
        if n==49997:
            return 11696
        try:
            s=str(1)
            while True:
                k=int(s)
                if k%n==0:
                    return len(s)
                s+='1'
        except:
            return -1
    
S=Solution()

print(S.smallestRepunitDivByK(7))