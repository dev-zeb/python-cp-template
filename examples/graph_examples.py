from python_cp_template import Graph

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)

print("DFS from node 0:")
g.dfs(0)
print("\nBFS from node 0:")
g.bfs(0)
