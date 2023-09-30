class Solution:
    def uncommonFromSentences(self,s1,s2):
        s1,s2=s1.split(' '),s2.split(' ')
        a,b=[i for i in s1 if s1.count(i)==1 and i not in s2],[i for i in s2 if s2.count(i)==1 and i not in s1]
        return a+b
    
s=Solution()

print(s.uncommonFromSentences("this apple is sweet","this apple is sour"))
print(s.uncommonFromSentences("apple apple","banana"))
print(s.uncommonFromSentences("s z z z s","s z ejt"))