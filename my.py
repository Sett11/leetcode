class Solution:
    def findRestaurant(self,a,b):
        s=list(set(a).intersection(set(b)))
        m=int(1e9)
        for i in range(len(s)):
            t=a.index(s[i])+b.index(s[i])
            m=min(t,m)
            s[i]=[s[i]]+[t]
        return [i[0] for i in s if i[1]==m]
    
s=Solution()

print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
print(s.findRestaurant(["happy","sad","good"],["sad","happy","good"]))