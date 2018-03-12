import numpy as np
import networkx as nx
import numpy.linalg as la
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
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
nx.draw_networkx_nodes(G, coord,node_size=34,node_color='k')

plt.show() 

A = nx.adjacency_matrix(G)
D = np.diag(np.ravel(np.sum(A,axis=1)))
L = D - A
l, U = la.eigh(L)
f = U[:,1]

labels = np.ravel(np.sign(f))
fig = plt.figure()
nx.draw_networkx_nodes(G, coord,node_size=45,node_color=labels)
plt.show()

k=3
means, labels = vq.kmeans2(U[:,1:k], k)
fig = plt.figure()
nx.draw_networkx_nodes(G, coord,node_size=45,node_color=labels)
plt.show()
