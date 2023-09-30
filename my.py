class Solution:
    def splitWordsBySeparator(self,w,s):
        return [j for j in sum([i.split(s) for i in w],[]) if j]
    
s=Solution()

print(s.splitWordsBySeparator(["one.two.three","four.five","six"],'.'))
print(s.splitWordsBySeparator(["$easy$","$problem$"],'$'))