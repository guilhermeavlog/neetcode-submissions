class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert to adjecency list
        D = defaultdict(list)

        for u, v in edges: 
            D[u].append(v)
            D[v].append(u)

        seen = set()

        def dfs_recursive(node):

            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    dfs_recursive(nei_node)

        count = 0 
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs_recursive(node)
                count += 1

        return count 
        

        
        