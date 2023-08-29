class Solution:
    def twoSum(self,a,n):
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]+a[j]==n:
                    return [i,j]
    
s=Solution()

print(s.twoSum([2,7,11,15],9))