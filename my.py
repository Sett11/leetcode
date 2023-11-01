class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_convert_to_array(h):
    r=[]
    c=h
    while c:
        r.append(c.val)
        c=c.next
    return r

def array_convert_to_list(a):
    L=ListNode()
    c=L
    l=len(a)
    for i in range(l):
            c.val=a[i]
            c.next=ListNode() if i!=l-1 else None
            c=c.next
    return L

class Solution:
    def getDecimalValue(self,h):
        return int(''.join(map(str,list_convert_to_array(h))),2)

s=Solution()

print(s.getDecimalValue(array_convert_to_list([1,0,1])))