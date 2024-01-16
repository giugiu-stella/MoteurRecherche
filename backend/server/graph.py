from collections import deque

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
    
    def calculate_betweenness_centrality(self):
        C_B = [0 for _ in range(len(self.nodes))]
        for s in self.nodes:
            S = deque()
            P = dict()
            sigma = dict()
            d = dict()
            
            for w in self.nodes:
                if w == s:
                    sigma[w] = 1
                    d[w] = 0
                else:
                    sigma[w] = 0
                    d[w] = -1
                P[w] = []
            
            Q = deque()
            Q.append(s)
            
            while len(Q) != 0:
                v = Q.popleft()
                S.append(v)
                
                for w in v.neighbors:
                    if d[w] < 0:
                        Q.append(w)
                        d[w] = d[v] + 1

                if d[w] == d[v] + 1:
                    sigma[w] = sigma[w] + sigma[v]
                    P[w].append(v)
            
            delta = {v : 0 for v in self.nodes}
            while len(S) != 0:
                w = S.popleft()
                for v in P[w]:
                    delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
                if w != s:
                    C_B[w] += delta[w]
                    
        self.nodes.sort(key=lambda x: C_B[x])    
    
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