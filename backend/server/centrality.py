from collections import deque
from server.graph import WeightedGraph, UnweightedGraph
from enum import Enum, auto

class Centrality(Enum):
    CLOSENESS = auto()
    BETWEENNESS = auto()

def compute_betweenness_centrality(G : UnweightedGraph):
        C_B = {w : 0 for w in G.nodes}
        for s in G.nodes:
            S = deque()
            P = dict()
            sigma = dict()
            d = dict()
            
            for w in G.nodes:
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
                           
        
            delta = {v : 0 for v in G.nodes}
            
                
            while len(S) != 0:
                w = S.pop()
                for v in P[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
                if w != s:
                    C_B[w] += delta[w]

        for w in G.nodes:
            w.centrality_measure = C_B[w]
            
def compute_closeness_centrality(G : WeightedGraph):
    n = len(G.nodes)
    for node in G.nodes:
        distance = sum(node.neighbors.values())
        node.centrality_measure = 0 if distance == 0 else (n -1) / distance
        