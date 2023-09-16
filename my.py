class Solution:
    def accountsMerge(self,a):
        a=sorted([i[:1]+sorted(i[1:]) for i in a])
        r=[]
        while a:
            t=[]
            t.extend(a.pop(0))
            name=t.pop(0)
            j=0
            while j<len(a):
                if set(t).intersection(a[j][1:]):
                    t.extend(a.pop(j)[1:])
                    j=-1
                j+=1
            r.append([name]+sorted(set(t)))
        return r

    
s=Solution()

print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                       ["John","johnsmith@mail.com","john00@mail.com"],
                       [ "Mary","mary@mail.com"],
                       ["Jhon","johnnybravo@mail.com"]]))

print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))