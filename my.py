class Solution:
    def decompressRLElist(self,a):
        return sum([[[a[i+1]]*a[i]][0] for i in range(0,len(a),2)],[])
    
s=Solution()

print(s.decompressRLElist([1,2,3,4]))
print(s.decompressRLElist([1,1,2,3]))