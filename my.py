from re import sub

class Solution:
    def maskPII(self,s):
        s=sub(r'[^\dA-z@\.]','',s)
        if s.isdigit():
            c=s[:-10]
            q=s[-10:]
            x=q[-4:]
            q=q[:-4]
            return ('+'+'*'*len(c)+'-' if c else '')+'-'.join([sub(r'.','*',q[i:i+3]) for i in range(0,len(q),3)])+'-'+x
        s=s.lower().split('@')
        return s[0][0]+('*'*5)+s[0][-1]+'@'+s[1]
    
s=Solution()

print(s.maskPII('LeetCode@LeetCode.com'))
print(s.maskPII('AB@qq.com'))
print(s.maskPII('1(234)567-890'))
print(s.maskPII('86-(10)12345678'))