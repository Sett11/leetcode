class Solution:
    def jump(self,a):
        a=[i+j for i,j in enumerate(a)]
        i=j=k=0
        while j<len(a)-1:
            k+=1
            i,j=j+1,max(a[i:j+1])
        return k
    
s=Solution()

print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))
print(s.jump([1,2,3]))
print(s.jump([1,2]))
print(s.jump([1,3,2]))
print(s.jump([1,2,3,4,5]))