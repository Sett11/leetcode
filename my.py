class Solution:
    def removeAnagrams(self,a):
        i=0
        while i<len(a)-1:
            if sorted(a[i])==sorted(a[i+1]):
                a.pop(i+1)
            else:
                i+=1
        return a
    
s=Solution()

print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"]))