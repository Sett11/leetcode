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
    def mergeNodes(self,h):
        a=list_convert_to_array(h)
        ind=[i for i,j in enumerate(a) if not j]
        return array_convert_to_list([sum(a[ind[i]+1:ind[i+1]]) for i in range(len(ind)-1)])

s=Solution()

print(s.mergeNodes(array_convert_to_list([0,14,13,0,40,0])))