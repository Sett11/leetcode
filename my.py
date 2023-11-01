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
    def rotateRight(self,h,k):
        r=list_convert_to_array(h)
        if not r:
            return h
        k%=len(r)
        r=(r[-k:]+r[0:-k])[::-1]
        c=h
        while len(r):
            c.val=r.pop()
            c=c.next
        return h

s=Solution()

print(s.rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),10**9+2))