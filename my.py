from re import sub

class Solution:
    def findMaxConsecutiveOnes(self,a):
        s=sub(r'(.)\1*',lambda e:' '+e.group()+' ' if e.group()[0]=='0' else str(len(e.group())),''.join([str(i) for i in a])).split(' ')
        return max([int(i) for i in s if i])
    
s=Solution()

print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(s.findMaxConsecutiveOnes([0]))