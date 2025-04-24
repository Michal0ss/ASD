import time
import matplotlib.pyplot as plt
import networkx as nx
from BFS import order_bfs
from DFS import order_dfs
from GraphsAlg.Shortest_path.bfs_path import bfs_shortest_path
from GraphsAlg.Shortest_path.dijkstra_path import dijkstra


def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G,pos,with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(1)


def generate_connected_random_graph(n,m):
    while True:
        G=nx.gnm_random_graph(n,m)
        if nx.is_connected(G):
            return G


#G = nx.Graph()
#G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
G=generate_connected_random_graph(20,20)
pos=nx.spring_layout(G)


"""odkomentowac w zaleznosci jaka wizualizacje chce sie zoabczyc"""

#visualize_search(order_bfs(G, 0), 'BFS Visualization', G, pos) # BFS
#visualize_search(order_dfs(G, 0), 'DFS Visualization', G, pos)
visualize_search(bfs_shortest_path(G, 0, 10), 'Shortest path Visualization', G, pos)
print(bfs_shortest_path(G, 0, 10))