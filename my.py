class Solution:
    def invalidTransactions(self,a):
        for i in range(len(a)):
            t=a[i].split(',')
            t[1],t[2]=int(t[1]),int(t[2])
            a[i]=t
        
        s=set(i[0] for i in a)
        o={}
        r=[]
        cache=[]
        for i in s:
            for j in a:
                if i==j[0]:
                    if o.get(i):
                        o[i].append(j)
                    else:
                        o[i]=[j]
        for i in o:
            t=o[i]
            for j in range(len(t)):
                if t[j][2]>1000 and [t[j],j] not in cache:
                    r.append(','.join([str(h) for h in t[j]]))
                    cache.append([t[j],j])
                for k in range(j+1,len(t)):
                    if abs(t[k][1]-t[j][1])<=60 and t[j][3]!=t[k][3]:
                        if [t[j],j] not in cache:
                            r.append(','.join([str(h) for h in t[j]]))
                            cache.append([t[j],j])
                        if [t[k],k] not in cache:
                            r.append( ','.join([str(h) for h in t[k]]))
                            cache.append([t[k],k])
        return r
        
    
s=Solution()

print(s.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print(s.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
print(s.invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]))
print(s.invalidTransactions(["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]))
print(s.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))