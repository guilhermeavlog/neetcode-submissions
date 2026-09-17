class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # to be valid tree number of edges must be n - 1
        # no loops

        if len(edges) != n - 1:
            return False

        D = defaultdict(list)

        for edge in edges:
            D[edge[0]].append(edge[1])
            D[edge[1]].append(edge[0])

        def cycle_detection(node, prev):

            for nei_node in D[node]:
                if nei_node == prev:
                    continue
                if nei_node not in seen:
                    seen.add(nei_node)
                    cycle_detection(nei_node, node)
                else:
                    return False
            
            return True 

        ans = 1
        for i in range(n):
            seen = set()
            seen.add(i)
            ans = ans and cycle_detection(i, None) 

        return ans

        