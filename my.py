class Solution:
    def findErrorNums(self,a):
        t=k=0

        for i in a:
            if a.count(i)>1:
                if i>0:
                    t=i
                    break
                
        for i in range(1,max(a)+2):
            if i not in a:
                k=i
                break

        return [t,k]


s=Solution()

print(s.findErrorNums([1,2,2,4]))
print(s.findErrorNums([1,1]))
print(s.findErrorNums([2,2]))
print(s.findErrorNums([1,2,3,4,5,6,7,8,9,10,11,11,13,14,15,16,17,18,19,20]))