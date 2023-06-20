class Solution:
    def lengthOfLongestSubstring(self,s):
        if(len(s)==len(set(s))):
            return len(s)
        m=i=0
        while i<len(s):
            j=i
            while j<=len(s):
                a=s[i:j]
                if(j==len(s)):
                    if(len(set(a))==len(a)):
                        m=max(len(a),m)
                        break
                if(len(set(a))<len(a)):
                    m=max(len(a)-1,m)
                    break
                j+=1
            i+=1
        return m
    
r=Solution()
print(r.lengthOfLongestSubstring('abcabcbb'))
print(r.lengthOfLongestSubstring('pwwkew'))
print(r.lengthOfLongestSubstring('aab'))
print(r.lengthOfLongestSubstring('dvdf'))
print(r.lengthOfLongestSubstring('anviaj'))