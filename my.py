class Solution:
    def findUnsortedSubarray(self,a):
        b=sorted(a)
        if a==b:
            return 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                for j in range(i,len(a)+1):
                    if j==len(a):
                        return j-i
                    if a[j:]==b[j:]:
                        return j-i
        return len(a)

s=Solution()

print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(s.findUnsortedSubarray([2,3,3,2,4]))
print(s.findUnsortedSubarray([1,3,2,2,2]))
print(s.findUnsortedSubarray([1,2]))