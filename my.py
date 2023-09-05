def sorted_one_count(x):
    return [i for i in x if x.count(i)==1]

class Solution:
    def countWords(self,a,b):
        return len(set(sorted_one_count(a)).intersection(set(sorted_one_count(b))))

s=Solution()

print(s.countWords(["leetcode","is","amazing","as","is"],["amazing","leetcode","is"]))