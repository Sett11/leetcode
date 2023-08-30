class Solution:
    def repeatedStringMatch(self,s,t):
        c,q=0,s
        n=len(t)//len(s)
        if ''.join([s]*n)==t:
            return n
        while c<50:
            if s.find(t)!=-1:
                return c+1
            s+=q
            c+=1
        return -1
    
s=Solution()

print(s.repeatedStringMatch('abcd','cdabcdab'))
print(s.repeatedStringMatch('abc','cabcabca'))
print(s.repeatedStringMatch('a','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))