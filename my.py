class Solution:
    def isNumber(self,s):
        try:
            float(s)
            s=s.lower()
            if(s=='-inf' or s=='+inf' or s=='-infinity' or s=='+infinity' or s.isalpha()):
                return False
            return True
        except:
            return False

r=Solution()
print(r.isNumber("inf"))