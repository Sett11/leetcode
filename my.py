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
    def mergeKLists(self,a):
        s=sum([list_convert_to_array(i) for i in a],[])
        return array_convert_to_list(sorted(s)) if s else None

s=Solution()

print(s.mergeKLists([array_convert_to_list(i) for i in [[1,4,5],[1,3,4],[2,6]]]))