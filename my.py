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
    def addTwoNumbers(self,a,b):
        a=list(map(int,str(int(''.join(map(str,list_convert_to_array(a))))+int(''.join(map(str,list_convert_to_array(b)))))))
        n=len(a)
        h=ListNode()
        c=h
        for i in range(n):
            c.val=a[i]
            c.next=ListNode() if i!=n-1 else None
            c=c.next
        return h

s=Solution()

print(s.addTwoNumbers(ListNode(7,ListNode(2,ListNode(4,ListNode(3)))),ListNode(5,ListNode(6,ListNode(4)))))