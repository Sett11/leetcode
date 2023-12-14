class Solution:
    def maxConsecutive(self,l,r,b):
        s=set(b)
        a=[l]+sorted(b)+[r]
        m=0
        for i in range(1,len(a)):
            m=max(a[i]-a[i-1]-(1 if a[i] in s and a[i-1] in s else 0),m)
        return m if m>1 else 0
    
S=Solution()

print(S.maxConsecutive(2,9,[4,6]))
print(S.maxConsecutive(28,50,[35,48]))