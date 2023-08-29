class Solution:
    def repeatedCharacter(self,s):
        a=[]
        for i in s:
            if i in a:
                return i
            else:
                a.append(i)
    
s=Solution()

print(s.repeatedCharacter('abccbaacz'))