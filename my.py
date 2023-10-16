from re import sub

class Solution:
    def checkZeroOnes(self,s):
        a=[i for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',s).split(' ') if i]
        b=c=0
        for i in a:
            if i[0]=='1':
                b=max(len(i),b)
            else:
                c=max(len(i),c)
        return b>c

s = Solution()

print(s.checkZeroOnes('11101000'))