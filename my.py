class Solution:
    def isNStraightHand(self,a,n):
        if len(a)%n:
            return False
        a.sort()
        r=[]
        while a:
            if len(r)==n:
                r=[]
            if not r:
                t=a.pop(0)
                r.append(t)
            if a and r[-1]+1 in a:
                r.append(a.pop(a.index(r[-1]+1)))
            if a and r[-1]+1 not in a and len(r)!=n:
                if a:
                    return False or n==1
                else:
                    break
        return True
    
s=Solution()

print(s.isNStraightHand([1,2,3,6,2,3,4,7,8],3))
print(s.isNStraightHand([1,1,2,2,3,3],3))
print(s.isNStraightHand([2,3,2,2,1,6,8,5,7,6],1))
print(s.isNStraightHand([9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21 ,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15 ,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21 ,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11 ],10))