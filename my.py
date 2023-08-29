class Solution:
    def majorityElement(self,a):
        l,s,r=len(a)/3,set(a),[]
        for i in s:
            if a.count(i)>l:
                r.append(i)
        return r
    
s=Solution()

print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,2]))