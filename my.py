class Solution:
    def orderlyQueue(self,s,k):
        if k!=1:
            return ''.join(sorted(s))
        a=[s]
        for i in range(len(s)):
            s=s[1:]+s[0]
            a.append(s)
        return sorted(a)[0]
    
S=Solution()

print(S.orderlyQueue('irsxx',1))