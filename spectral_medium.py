import numpy as np
import networkx as nx
import numpy.linalg as la
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt

G = nx.powerlaw_cluster_graph(100, 1, 0.0)
print("Node Degree")

for v in G:
    print('%s %s' % (v, G.degree(v)))

nx.draw_circular(G, with_labels=True)
plt.show()


coord = nx.spring_layout(G, iterations=1000)

fig = plt.figure()
axs = fig.add_subplot(111, aspect='equal')
axs.axis('off')

nx.draw_networkx_edges(G, coord)
nx.draw_networkx_nodes(G, coord,node_size=100,node_color='k')

plt.show() 

A = nx.adjacency_matrix(G)
D = np.diag(np.ravel(np.sum(A,axis=1)))
L = D - A
l, U = la.eigh(L)
f = U[:,1]

labels = np.ravel(np.sign(f))
fig = plt.figure()
nx.draw_networkx_nodes(G, coord,node_size=100,node_color=labels)
plt.show()

for k in list(range(3,10,2)):
    print(k)
    means, labels = vq.kmeans2(U[:,1:k], k)
    fig = plt.figure()
    nx.draw_networkx_nodes(G, coord,node_size=100,node_color=labels)
    plt.show()
