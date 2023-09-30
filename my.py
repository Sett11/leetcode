class Solution:
    def balancedStringSplit(self,s):
        r=[]
        i=0
        while i<len(s):
            c=s[i]
            j=i+1
            while j<=len(s):
                if c.count('L')==c.count('R'):
                    r.append(c)
                    i=j-1
                    break
                else:
                    c+=s[j]
                    j+=1
            i+=1
        return len(r)
    
s=Solution()

print(s.balancedStringSplit('RLRRLLRLRL'))
print(s.balancedStringSplit('RLRRRLLRLL'))