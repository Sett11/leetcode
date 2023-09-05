class Solution:
    def minimumLength(self,s):
        if len(s)<=1:
            return len(s)
        while len(s)>1 and s[0]==s[-1]:
            i=0
            while i<len(s)-1 and s[i]==s[i+1]:
                i+=1
            j=len(s)-1
            while j and s[j]==s[j-1] and j!=i:
                j-=1
            s=s[i+1:j]
        return len(s)
    
s=Solution()

print(s.minimumLength('ca'))
print(s.minimumLength('cabaabac'))
print(s.minimumLength('aabccabba'))
print(s.minimumLength('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbbccbcbcbccbbabbb'))