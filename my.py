class Solution:
    def calculate(self,s):
        return eval(s.replace('/','//'))
    
s=Solution()

print(s.calculate('3/2'))