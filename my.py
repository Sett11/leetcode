class Solution:
    def finalString(self,s):
        c=''
        for i in s:
            if i!='i':
                c+=i
            else:
                c=c[::-1]
        return c
    
s=Solution()

print(s.finalString('string'))
print(s.finalString('poiinter'))