class Solution:
    def nextGreaterElements(self,a):
        r=[]
        a+=a
        for i in range(len(a)//2):
            v=False
            for j in range(i+1,len(a)):
                if a[j]>a[i]:
                    r.append(a[j])
                    v=True
                    break
            if not v:
                r.append(-1)
        return r

s=Solution()

print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([1,2,3,4,3]))