from re import sub

def f(s,n):
    k=str(round(float(s[1:])/100*(100-n),2))
    return ' $'+k+('0' if len(k.split('.')[1])<2 else '')+' '

class Solution:
    def discountPrices(self,s,n):
        s=' '+s+' '
        s=sub(r'\s\$\d+\s',lambda x:' '+x.group()+' ',s)
        return sub(r'\s\$\d+\s',lambda x:f(x.group().strip(),n),s).strip().replace('  ',' ')

S=Solution()

print(S.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$",100))
print(S.discountPrices("ka3caz4837h6ada4 r1 $602",9))
print(S.discountPrices("there are $1 $2 and 5$ candies in the shop",50))