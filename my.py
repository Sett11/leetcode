from re import sub
def f(x):
    return all(x%i for i in range(2,int(x**.5)+1)) and x>1

class Solution:
    def countPrimeSetBits(self,a,b):
        return len([i for i in range(a,b+1) if f(len(sub(r'[^1]','',bin(i))))])
    
s=Solution()

print(s.countPrimeSetBits(10,15))