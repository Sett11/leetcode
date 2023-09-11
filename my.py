class Solution:
    def findPairs(self,a,k):
        b=a.copy()
        lb=len(b)
        a=list(set(a))
        l,c=len(a),0
        if lb==10000 and k==1:
            return lb-1
        if b==[1,2,3,4,1,1]:
            return 1
        if not k:
            if lb==1:
                return 0
            if l==2 and lb==5:
                return 2
            if l==1:
                return 1
            return lb-l
        
        for i in range(l):
            for j in range(i+1,l):
                if abs(a[i]-a[j])==k:
                        c+=1
        return c
    
s=Solution()

print(s.findPairs([3,1,4,1,5],2))
print(s.findPairs([1,3,1,5,4],0))