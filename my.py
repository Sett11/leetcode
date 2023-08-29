class Solution:
    def searchInsert(self,a,n):
        if n in a:
            return a.index(n)
        for i in range(len(a)):
            if a[i]>n:
                return i
        return len(a)
    
s=Solution()

print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))