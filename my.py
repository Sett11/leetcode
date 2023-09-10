def primes_checker(n):
    return all(n%i for i in range(2,int(n**.5)+1)) and n>=2

class Solution:
    def diagonalPrime(self,a):
        m=0
        for i in range(len(a)):
            t=[j for j in [a[i][len(a[i])-i-1],a[i][i]] if primes_checker(j)]
            m=max(m,max(t,default=0))
        return m
    
s=Solution()

print(s.diagonalPrime([[1,2,3],
                       [5,6,7],
                       [9,10,11]]))