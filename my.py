k=2

def guess(n):
    if n<k:
        return 1
    if n>k:
        return -1
    return 0

class Solution:
    def guessNumber(self,n):
        l,r=0,n+1

        while True:
            m=(l+r)//2
            x=guess(m)
            if x==0:
                return m
            elif x==1:
                l=m
            else:
                r=m

S=Solution()

print(S.guessNumber(2))