class Solution:
    def minimumRightShifts(self,a):
        i=0
        b=sorted(a)
        while i<len(a):
            if a==b:
                break
            a.insert(0,a.pop())
            i+=1
        return -1 if i==len(a) else i


s = Solution()

print(s.minimumRightShifts([2,1,4]))
