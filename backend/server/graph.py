
class Node:
    def __init__(self, json):
        self.json = json
        self.neighbors = []
        self.centrality_measure = -1

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def set_value(self, centrality_measure ):
        self.centrality_measure = centrality_measure 

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node
    
    def sort_nodes_by_centrality_measure(self):
        self.nodes.sort(key=lambda x: x.centrality_measure)
        
    def get_json_nodes(self):
        return [node.json for node in self.nodes]
        
    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

        node1.add_neighbor(node2)
        node2.add_neighbor(node1)