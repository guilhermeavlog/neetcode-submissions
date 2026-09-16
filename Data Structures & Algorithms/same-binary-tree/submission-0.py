# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(start_node):
            queue = deque([start_node])
            values = []

            while queue:
                node = queue.popleft()

                if node is None: # add none elements
                    values.append(None)
                    continue

                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            return values

        if bfs(p) == bfs(q):
            return True
        
        return False




        