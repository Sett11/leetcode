def f(s,n):
    return s if not n else f(''.join([str(j) for j in str(sum([int(i) for i in s]))]),n-1)

class Solution:
    def getLucky(self,s,n):
        return int(f(''.join([str(ord(i)-96) for i in s]),n))
        
    
s=Solution()

print(s.getLucky('zbax',2))
print(s.getLucky('iiii',1))