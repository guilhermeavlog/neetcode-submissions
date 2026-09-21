"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
            
        seen = set()
        seen.add(node)
        mapping = dict() 

        def dfs(node):
            clone_node = Node()
            clone_node.val = node.val 
            mapping[node] = clone_node
            
            for nei_node in node.neighbors:
                if nei_node not in seen:
                    seen.add(nei_node)
                    dfs(nei_node)   

        visited = set()
        visited.add(node)
        def dfs_connections(node):
            
            for nei_node in node.neighbors:
                mapping[node].neighbors.append(mapping[nei_node])
                if nei_node not in visited:
                    visited.add(nei_node)
                    dfs_connections(nei_node)

        dfs(node)
        dfs_connections(node)
        
        return mapping[node]

        


        