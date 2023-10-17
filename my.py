def gcd(x,y):
    return  [i for i in range(1,min(x,y)+1) if x%i==0 and y%i==0]==[1]

class Solution:
    def countBeautifulPairs(self,a):
        c=0
        l=len(a)
        for i in range(l):
            for j in range(i+1,l):
                if gcd(int(str(a[i])[0]),int(str(a[j])[-1])):
                    c+=1
        return c
    
s=Solution()

print(s.countBeautifulPairs([31,25,72,79,74]))