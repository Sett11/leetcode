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

class Solution:
    def reorderList(self,h):
        r=list_convert_to_array(h)
        n=len(r)
        a=sum([[r[i],r[n-i-1]] for i in range(n//2)]+([[r[n//2]]] if n&1 else []),[])
        c=h
        for i in a:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))