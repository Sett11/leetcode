class Solution:
    def canJump(self,a):
        if len(a)==1:
            return True
        try:
            a=[i+j for i,j in enumerate(a)]
            i=j=k=0
            while j<len(a)-1:
                k+=1
                i,j=j+1,max(a[i:j+1])
            return k
        except:
            return False
    
s=Solution()

print(s.canJump([2,3,1,1,4]))
print(s.canJump([2,3,0,1,4]))
print(s.canJump([1,2,3]))
print(s.canJump([1,2]))
print(s.canJump([1,3,2]))
print(s.canJump([3,2,1,0,4]))