class Solution:
    def stringMatching(self,a):
        l=len(a)
        r=[]
        for i in range(l):
            for j in range(l):
                if a[i] in a[j] and i!=j:
                    r.append(a[i])
                    break
        return r
    
s=Solution()

print(s.stringMatching(["mass","as","hero","superhero"]))