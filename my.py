class Solution:
    def removeDuplicates(self,a):
        i=0
        while i<len(a):
            if a.count(a[i])>1:
                a.pop(i)
                i-=1
            i+=1
        return len(a)
    
s=Solution()

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1,1,1,1]))