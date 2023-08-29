class Solution:
    def moveZeroes(self,a):
        l,i=len(a),0
        while i<l:
            if not a[i]:
                a.append(a.pop(i))
                l-=1
                i-=1
            i+=1
        return a
    
s=Solution()

print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([0,0,1]))