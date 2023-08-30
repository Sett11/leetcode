from re import sub

class Solution:
    def compress(self,a):
        r=list(''.join([i if len(i)==1 else i[0]+str(len(i)) for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',''.join(a)).split(' ') if i]))
        a.clear()
        [a.append(i) for i in r]
        return len(r)
    
q=["a","a","b","b","c","c","c"]

s=Solution()

print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(s.compress(q))
print(q)
print(s.compress(["a"]))