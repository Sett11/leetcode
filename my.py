class Solution:
    def maxRepeating(self,s,c):
        x=c
        n=0
        while c in s:
            c+=x
            n+=1
        return n

s=Solution()

print(s.maxRepeating('ababababakdk','ab'))