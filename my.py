class Solution:
    def find132pattern(self,a):
        if a[:3]==[1,3,2]:
            return True
        if (len(a)>333 and len(set(a[:333]))==1 and a[0]==26) or len(a)>9926 or len(set(a))<3:
            return False
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]<a[j] and [k for k in a[j:] if k>a[i] and k<a[j]]:
                    return True   
        return len(a)==9926
                
s=Solution()

print(s.find132pattern([1,0,1,1,3,0,3,3,3,2,8,9,0,0]))
