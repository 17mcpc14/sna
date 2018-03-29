import numpy as np
import networkx as nx
import numpy.linalg as la
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt
import collections

# generate power graph based on barabasi albert model 
G = nx.barabasi_albert_graph(100, 1, 0.0)

# print the graph
coord = nx.spring_layout(G, iterations=1000)
fig = plt.figure()
axs = fig.add_subplot(111, aspect='equal')
axs.axis('off')
nx.draw_networkx_edges(G, coord)
nx.draw_networkx_nodes(G, coord,node_size=100,node_color='k')
plt.show() 

# degree distribution analysis
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Degree Distribution")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

#eigen value centrality analysis
print("Eigen value centralities...")
centrality=nx.eigenvector_centrality_numpy(G)
print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
phi = max(centrality)

#katz centrality analysis
print("Katz centralities :")
centrality = nx.katz_centrality(G,1/phi-0.01)
for n,c in sorted(centrality.items()):
   print("%d %0.2f"%(n,c))
print( "Avg. katz centrality : ", sum(centrality)/len(centrality), "Max. katz centrality : ", max(centrality))

degreeCount = collections.Counter(centrality)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Katz Centrality Distribution")
plt.ylabel("Count")
plt.xlabel("Centrality")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# Clustering analysis
clustering = nx.clustering(G.to_undirected())
print("Clustering coefficients : ", clustering)
print( "Avg. clustering : ", nx.average_clustering(G.to_undirected()), "Max. clustering : ", max(clustering))

degreeCount = collections.Counter(clustering)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Katz Clustering Distribution")
plt.ylabel("Count")
plt.xlabel("Clustering")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
