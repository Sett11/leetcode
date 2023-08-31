def merge(a):
        a=sorted(a,key=lambda e:(e[0],e[1]))
        i=0
        while i<len(a)-1:
            if a[i][0]<=a[i+1][0] and a[i][1]<=a[i+1][1] and a[i][1]>=a[i+1][0]:
                a[i][1]=a[i+1][1]
                a.pop(i+1)
                i-=1
            if len(a)==1:
                break
            if a[i][0]<=a[i+1][0] and a[i][1]>=a[i+1][1]:
                a.pop(i+1)
                i-=1
            i+=1
        return a

class Solution:
    def insert(self,a,b):
         if not a:
              return [b]
         i=0
         while i<len(a):
              if a[i][1]>=b[0]:
                   a.insert(i+1,b)
                   break
              i+=1
         if b not in a:
              a.append(b)
         return merge(a)
    
s=Solution()

print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))