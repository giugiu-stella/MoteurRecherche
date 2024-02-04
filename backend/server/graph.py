class Node:
    def __init__(self, json):
        self.json = json
        self.centrality_measure = -1

    
class NodeUnweighted(Node):
    def __init__(self, json) -> None:
        super().__init__(json)
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
class NodeWeighted(Node):
    def __init__(self, json) -> None:
        super().__init__(json)
        self.neighbors = dict()
        
    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

class Graph:
    def __init__(self):
        self.nodes = []
    
    def sort_nodes_by_centrality_measure(self, ordre):
        if ord == "descending":
            self.nodes.sort(key=lambda x: -x.centrality_measure)
        else:
            self.nodes.sort(key=lambda x: x.centrality_measure)
        
    def get_json_nodes(self):
        return [node.json for node in self.nodes]
        
        
class UnweightedGraph(Graph):
    def __init__(self):
        super().__init__()
    
    def add_node(self, value):
        node = NodeUnweighted(value)
        self.nodes.append(node)
        
    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
        
class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def add_node(self, value):
        node = NodeWeighted(value)
        self.nodes.append(node)
        
    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

        node1.add_neighbor(node2, weight)
        node2.add_neighbor(node1, weight)


def brandes_betweenness_centrality(graph):
    betweenness = {node: 0.0 for node in graph.nodes()}

    for source in graph.nodes():
        stack = []
        predecessors = {node: [] for node in graph.nodes()}
        sigma = {node: 0 for node in graph.nodes()}
        sigma[source] = 1
        distance = {node: -1 for node in graph.nodes()}
        distance[source] = 0
        queue = [source]

        while queue:
            current_node = queue.pop(0)
            stack.append(current_node)

            for neighbor in graph.neighbors(current_node):
                if distance[neighbor] < 0:
                    queue.append(neighbor)
                    distance[neighbor] = distance[current_node] + 1

                if distance[neighbor] == distance[current_node] + 1:
                    sigma[neighbor] += sigma[current_node]
                    predecessors[neighbor].append(current_node)

        delta = {node: 0 for node in graph.nodes()}

        while stack:
            current_node = stack.pop()
            for predecessor in predecessors[current_node]:
                delta[predecessor] += (sigma[predecessor] / sigma[current_node]) * (1 + delta[current_node])
            if current_node != source:
                betweenness[current_node] += delta[current_node]

    return betweenness    
    
