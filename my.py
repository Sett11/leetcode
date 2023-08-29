class Solution:
    def countCharacters(self,a,s):
        return len(''.join([i for i in a if all([j in s and i.count(j)<=s.count(j) for j in i])]))
    
s=Solution()

print(s.countCharacters(["cat","bt","hat","tree"],'atach'))
print(s.countCharacters(["hello", "world", "leetcode"],'welldonehoneyr'))