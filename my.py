class Solution:
    def capitalizeTitle(self,s):
        return ' '.join([i.capitalize() if len(i)>2 else i.lower() for i in s.split(' ')])
    
s=Solution()

print(s.capitalizeTitle("capiTalIze tHe titLe"))
print(s.capitalizeTitle("First leTTeR of EACH Word"))