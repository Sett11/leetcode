from re import sub

class Solution:
    def maxNumberOfBalloons(self,s):
        if not all(i in s for i in 'balon'):
            return 0
        a=sub(r'(.)\1*',lambda e:' '+e.group(),''.join(sorted(sub(r'[^balon]','',s)))).split(' ')[1:]
        m=1e5
        for i in a:
            if i[0]=='l' or i[0]=='o':
                m=min(len(i)//2,m)
            else:
                m=min(len(i),m)
        return m
    
s=Solution()

print(s.maxNumberOfBalloons("loonbalxballpoon"))