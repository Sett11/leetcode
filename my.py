def search_letter(s,c):
    alf='abcdefghijklmnopqrstuvwxyz'
    for i in alf:
        if i!=s and i!=c:
            return i

class Solution:
    def modifyString(self,s):
        s=list(s)
        for i in range(len(s)):
            if s[i]=='?':
                if i==0 and i==len(s)-1:
                    s[i]='a'
                if i==0 and s[i]=='?':
                    q=search_letter(s[i+1],s[i+1])
                    s[i]=q
                elif i==len(s)-1 and s[i]=='?':
                    q=search_letter(s[i-1],s[i-1])
                    s[i]=q
                elif s[i]=='?':
                    q=search_letter(s[i-1],s[i+1])
                    s[i]=q
        return ''.join(s)

    
s=Solution()

print(s.modifyString(s.modifyString('ubv?w')))