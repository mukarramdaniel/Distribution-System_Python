
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node, weight, data):
        self.graph[node] = (weight, data)
    
    def make_complete(self):
        for node1 in self.graph:
            for node2 in self.graph:
                if node1 != node2:
                    self.graph[node1][1].append((node2, self.graph[node2][0]))
    
    def get_edges(self, node):
        return self.graph[node][1]
    def prinT(self):
        print(self.graph)
    
    def minimum_spanning_tree(self):
        mst = []
        visited = set()
        current_node = next(iter(self.graph))
        visited.add(current_node)
        
        while len(visited) < len(self.graph):
            min_weight = float("inf")
            min_edge = None

            for node in visited:
                for edge in self.get_edges(node):
                    if edge[0] not in visited:
                        if edge[1] < min_weight:
                            min_weight = edge[1]
                            min_edge = (node, edge[0])
            
            mst.append(min_edge)
            current_node = min_edge[1]
            visited.add(current_node)
        
        return mst

# g = Graph()
# g.add_node(11, 1, [])
# g.add_node(12, 2, [])
# g.add_node(13, 3, [])
# g.make_complete()
# print(g.prinT())
# print(g.minimum_spanning_tree())  
