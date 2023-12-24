class Solution:
    def getStrongest(self,a,k):
        n=sorted(a)[(len(a)-1)//2]
        return sorted(a,key=lambda x:(abs(x-n),x),reverse=True)[:k]
    
S=Solution()

print(S.getStrongest([1,2,3,4,5],2))
print(S.getStrongest([-7,22,17,3],2))