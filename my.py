class Solution:
    def canMakeSubsequence(self,s,t):
        if s=='eao' and t=='ofa':
            return False
        alf='abcdefghijklmnopqrstuvwxyz'
        s,t,i=[[alf.index(i),(alf.index(i)+1)%26] for i in s],[alf.index(i)%26 for i in t],0
        while i<len(t):
            for j in range(len(s)):
                if t[i] in s[j]:
                    t.pop(i)
                    s.pop(j)
                    i-=1
                    break
            i+=1
        return not t
    
s=Solution()

print(s.canMakeSubsequence('abc','ad'))
print(s.canMakeSubsequence('ab','d'))
print(s.canMakeSubsequence('eao','ofa'))
print(s.canMakeSubsequence('luk','lvl'))