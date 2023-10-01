class Solution:
     def makeGood(self,s):
                i=0
                s=list(s)
                while i<len(s)-1:
                        if i<0:
                               i=0
                        if len(s)==1:
                               break
                        if (s[i].lower()==s[i+1].lower() and s[i+1].isupper() and s[i].islower()) or (s[i].lower()==s[i+1].lower() and s[i].isupper() and s[i+1].islower()):
                            s.pop(i)
                            s.pop(i)
                            i-=2
                        i+=1
                return ''.join(s)
    
s=Solution()

print(s.makeGood('leEeetcode'))
print(s.makeGood('abBAcC'))
print(s.makeGood('kkdsFuqUfSDKK'))