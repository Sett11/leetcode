class Solution:
    def heightChecker(self,a):
        c=0
        b=sorted(a)
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        return c
            
    
s=Solution()

print(s.heightChecker([1,1, 4 ,2, 1 , 3 ]))
print(s.heightChecker([5,1,2,3,4]))