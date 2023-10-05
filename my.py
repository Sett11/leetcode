class Solution:
    def greatestLetter(self,s):
        a=sorted(filter(lambda e:e.isupper(),[i for i in s if i.lower() in s and i.upper() in s]),key=ord,reverse=True)
        return a[0] if a else ''
    
s=Solution()

print(s.greatestLetter("arRAzFif"))