class Solution:
    def percentageLetter(self,s,t):
        return int(len([i for i in s if i==t])/len(s)*100)
    
s=Solution()

print(s.percentageLetter('foobar','o'))