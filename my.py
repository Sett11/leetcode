class Solution:
    def canThreePartsEqualSum(self,a):
        s=sum(a)//3
        r=[]
        t=[]
        i=0
        while i<=len(a):
            if len(r)==2 and r[0]==r[1]:
                if sum(t+a[i:])==r[0]:
                    return True
            if t and sum(t)==s:
                r.append(sum(t))
                t=[]
            t.append(a[i])
            i+=1
            if i==len(a):
                if t:
                    r.append(sum(t))
                break
        return len(r)==3 and len(set(r))==1

        
s=Solution()

print(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(s.canThreePartsEqualSum([0,0,0,0]))