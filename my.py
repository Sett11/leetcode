class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def inorderTraversal(self,r):
        a=[]
        def f(r):
            if not r:
                return
            f(r.left)
            a.append(r.val)
            f(r.right)
        f(r)
        return a

S=Solution()

print(S.inorderTraversal())