class Solution:
    def romanToInt(self,s):
        a=[['CM', 900],['M', 1000], ['CD', 400], ['D', 500], ['XC', 90], ['C', 100], ['XL', 40], ['L', 50], ['IX', 9], ['X', 10], ['IV', 4], ['V', 5], ['I', 1]]
        for i in a:
            s=s.replace(i[0],' '+str(i[1])+' ')
        return sum([int(i) for i in s.split(' ')if i])

s=Solution()

print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))