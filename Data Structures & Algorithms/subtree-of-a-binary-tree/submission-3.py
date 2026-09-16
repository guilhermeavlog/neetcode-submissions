# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def search(root, target):
            if not root:
                return []
            results = []
            if root.val == target:
                results.append(root)
            results.extend(search(root.left, target))
            results.extend(search(root.right, target))
            return results

        def preOrder(root):
            if not root:
                return []
            return [root.val] + preOrder(root.left) + preOrder(root.right)

        
        starting_nodes = search(root, subRoot.val)
        y = preOrder(subRoot)
    
        for node in starting_nodes:
            x = preOrder(node)
            if x == y:
                return True
        return False
        
            
        