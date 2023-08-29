class Solution:
    def rearrangeCharacters(self,s,t):
        if [i for i in t if i not in s]:
            return 0
        return int(min([s.count(i)/t.count(i) for i in set(s) if i in t]))
    
s=Solution()

print(s.rearrangeCharacters('ilovecodingonleetcode','code'))
print(s.rearrangeCharacters('abcba','abc'))
print(s.rearrangeCharacters('abbaccaddaeea','aaaaa'))
print(s.rearrangeCharacters('codecodecodecode','codecode'))