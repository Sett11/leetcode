class Solution:
    def similarPairs(self,a):
        a=[sorted(set(i)) for i in a]
        c=0
        l=len(a)
        for i in range(l):
            for j in range(i+1,l):
                if a[i]==a[j]:
                    c+=1
        return c
    
s=Solution()

print(s.similarPairs(["aba","aabb","abcd","bac","aabc"]))