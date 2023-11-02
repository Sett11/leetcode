# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def list_convert_to_array(h):
#     r=[]
#     c=h
#     while c:
#         r.append(c.val)
#         c=c.next
#     return r

# def array_convert_to_list(a):
#     L=ListNode()
#     c=L
#     l=len(a)
#     for i in range(l):
#             c.val=a[i]
#             c.next=ListNode() if i!=l-1 else None
#             c=c.next
#     return L

# class Solution:
#     def mergeKLists(self,a):
#         s=sum([list_convert_to_array(i) for i in a],[])
#         return array_convert_to_list(sorted(s)) if s else None

# s=Solution()

# s.mergeKLists([array_convert_to_list(i) for i in [[1,4,5],[1,3,4],[2,6]]]))

from collections import deque

class MyLinkedList:

    def __init__(self):
        self.val=0
        self.next=None
        self.list=deque()

    def get(self, index: int) -> int:
        return self.list[index] if index<len(self.list) else -1

    def addAtHead(self, val: int) -> None:
        self.list.appendleft(val)

    def addAtTail(self, val: int) -> None:
        self.list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        self.list.insert(index,val) if index<=len(self.list) else None

    def deleteAtIndex(self, index: int) -> None:
        if index<len(self.list):
            del self.list[index]


M=MyLinkedList()

M.addAtHead(1)
M.addAtTail(3)
M.addAtIndex(1,2)
print(M.get(1))

M.deleteAtIndex(1)

print(M.get(1))