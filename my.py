import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def divisibilityArray(self,s,n):
        a=[]
        c=''
        for i in range(len(s)):
            c+=s[i]
            if int(c)%n==0:
                a.append(1)
            else:
                a.append(0)
        return a

s = Solution()

print(s.divisibilityArray('998244353',3))
