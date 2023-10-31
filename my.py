class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self,h):
        c=h
        r=[]
        while c:
            r.append(c.val)
            c=c.next
        n=len(r)//2
        if not n:
            return h
        i=0
        c=h
        while c:
            if i==n-1:
                return c.next
            i+=1
            c=c.next

s=Solution()

print(s.middleNode(ListNode(3,ListNode(1,ListNode(4,ListNode(11,ListNode(9,ListNode(5,ListNode(15)))))))))