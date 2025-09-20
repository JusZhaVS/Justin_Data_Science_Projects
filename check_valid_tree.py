from typing import List, DefaultDict
from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges) != n-1):
            return False
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [(0,-1)]

        while stack:
            u, p = stack.pop()
            if u in visited:
                return False #we've detected a cycle
            
            visited.add(u)
            for neighbor in graph[u]:

                if neighbor == p: #don't want to include parents
                    continue

                stack.append((neighbor, u))

        return True