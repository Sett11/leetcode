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
    def removeNthFromEnd(self,h,k):
        a=list_convert_to_array(h)
        if len(a)==1 and k==1:
            return None
        del a[-k]
        return array_convert_to_list(a)

s=Solution()

print(s.removeNthFromEnd(array_convert_to_list([1,2,3,4,5]),2))