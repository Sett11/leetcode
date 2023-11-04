from copy import deepcopy

class Solution:
    def cloneGraph(self,node):
        c=deepcopy(node)
        return c