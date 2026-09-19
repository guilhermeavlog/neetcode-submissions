class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        directed graph, 
        if cycle we can't do all courses since it would fundamentally mean that course a requires course b but course b requires course a but we need to choose only one to take first     

        '''

        G = defaultdict(list)

        for a, b in prerequisites:
            G[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node] 

            if state == VISITED: return True
            elif state == VISITING: return False
            
            states[node] = VISITING

            for nei_node in G[node]:
                if not dfs(nei_node): return False

            states[node] = VISITED
            return True  
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        