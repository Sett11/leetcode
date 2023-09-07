class Solution:
    def partitionString(self,s):
        if len(set(s))==1:
            return len(s)
        s+=s[-1]
        c=0
        i=0
        while i<len(s):
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if len(t)!=len(set(t)):
                    c+=1
                    i=j-2
                    break
            i+=1
        return c
    
s=Solution()

print(s.partitionString('abacaba'))
print(s.partitionString('ssssss'))