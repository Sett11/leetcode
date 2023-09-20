class Solution:
    def reverseOnlyLetters(self,s):
        s=list(s)
        a=[]
        for i in range(len(s)):
            if s[i].isalpha():
                a.insert(0,s[i])
                s[i]='&6&'
        s=''.join(s)
        while a:
            s=s.replace('&6&',a.pop(0),1)
        return s
    
s=Solution()

print(s.reverseOnlyLetters('a-bC-dEf-ghIj!'))