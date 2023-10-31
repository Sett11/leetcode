class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self,h):
        c,r,l=h,[],0
        while c:
            r.append(c.val)
            c=c.next
            l+=1
        return max([r[i]+r[l-i-1] for i in range(l//2)])

s=Solution()

print(s.pairSum(ListNode(3,ListNode(1,ListNode(4,ListNode(11,ListNode(9,ListNode(5,ListNode(15,ListNode(2))))))))))