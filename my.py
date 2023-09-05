class Solution:
    def intersection(self,a):
        r=set(a.pop(0))
        a=[set(i) for i in a]
        for i in range(len(a)):
            r=r.intersection(a[i])
        return sorted(r)
    
s=Solution()

print(s.intersection([[1,2,3]]))
print(s.intersection([[ 3 ,1,2, 4 ,5],[1,2, 3 , 4 ],[ 3 , 4 ,5,6]]))
print(s.intersection([[73,6,87,26,12,83,19,43,31,63,54,21,70,10,16,97,40,93,65,99,53,61],[43, 74,83,53,67,8,16,72,9,50,45,97,79,88,80,12,26,46,30,70,13,84,100,40,60,4,6, 52],[76,86,40,90,15,44,43,70,61,2,95,10,93,74,6,99,96,47,48,26,82,16,84, 38,85,14]]))
print(s.intersection([[17,20],[20,25,49],[16,7,20,47,17]]))