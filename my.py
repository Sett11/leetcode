class Solution:
    def findKthPositive(self,a,k):
        n=1
        while k:
            if n not in a:
                k-=1
            n+=1
        return n-1
    
s=Solution()

print(s.findKthPositive([2,3,4,7,11],5))
print(s.findKthPositive([1,2],1))
print(s.findKthPositive([1,2,3,4],2))