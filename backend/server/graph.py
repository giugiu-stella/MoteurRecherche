from collections import deque
import networkx as nx

class Node:
    def __init__(self, json, id):
        self.json = json
        self.neighbors = []
        self.centrality_measure = -1
        self.id = id

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def set_value(self, centrality_measure ):
        self.centrality_measure = centrality_measure 
        

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value, value["id"])
        self.nodes.append(node)
        return node
    
    def calculate_betweenness_centrality(self):
        C_B = {w : 0 for w in self.nodes}
        for s in self.nodes:
            print(s)
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
                #print(f'v {v}')
                for w in v.neighbors:
                    #print(f'd[v] {d[v]}, d[w] {d[w]}')
                    if d[w] < 0:
                        Q.append(w)
                        d[w] = d[v] + 1
                        #print(d[w])

                    if d[w] == d[v] + 1:
                        sigma[w] = sigma[w] + sigma[v]
                        P[w].append(v)
                           
        
            delta = {v : 0 for v in self.nodes}
            
                
            while len(S) != 0:
                w = S.pop()
                print(f'w {w}')
                for v in P[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
                if w != s:
                    C_B[w] += delta[w]
                    
            for u in self.nodes:
                print(f'{u} : sigma = {sigma[u]}, delta = {delta[u]}, Cb = {C_B[u]}')
            print()
            
            
            #print(delta)
        for w in self.nodes:
            w.centrality_measure = C_B[w]
        #self.nodes(key=lambda x: C_B[x])    
    
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


if __name__ == "__main__":
    A = Node('a', None)
    B = Node('b', None)
    C = Node('c', None)
    D = Node('d', None)
    E = Node('e', None)
    F = Node('f', None)
    
    G = Graph()
    G.add_edge(A, B)
    G.add_edge(B, D)
    G.add_edge(A, C)
    G.add_edge(D, F)
    G.add_edge(E, A)
    #G.add_edge(F, D)
    G.add_edge(E, C)
    
    """for v in G.nodes:
        print(v)
        for w in v.neighbors:
            print(w)
        print()"""
    
    G.calculate_betweenness_centrality()
    for node in G.nodes:
        print(f'{node.id} {node.centrality_measure}')

    nx_graph = nx.Graph()
    for node in G.nodes:
        for v in node.neighbors:
            nx_graph.add_edge(node.id, v.id)

    # Calculer la centralité de l'intermédiarité
    betweenness_centrality = nx.betweenness_centrality(nx_graph)

    # Afficher la centralité de l'intermédiarité pour chaque nœud
    for node_label, centrality_value in betweenness_centrality.items():
        print(f"Nœud {node_label}: {centrality_value}")
        
    betweenness_centrality = brandes_betweenness_centrality(nx_graph)
    for node, centrality in betweenness_centrality.items():
        print(f"Nœud {node}: {centrality}")
    
    
    
