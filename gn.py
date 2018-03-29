import networkx as nx
import matplotlib.pyplot as plt
import collections

#generation of a forest fire graph with GN incremental growth model
G = nx.gn_graph(100, kernel=lambda x: x ** 1.5)

# Graph display
coord = nx.spring_layout(G, iterations=1000)
fig = plt.figure()
axs = fig.add_subplot(111, aspect='equal')
axs.axis('off')
nx.draw_networkx_edges(G, coord)
nx.draw_networkx_nodes(G, coord,node_size=100,node_color='k')
plt.show() 

# Degree distribution analysis
print("Degree Distribution :")
print(G.degree())
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
print( "Avg. degree : ", sum(deg)/len(deg), "Max. degree : ", max(deg), "Min. degree : ", min(deg))
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Degree Distribution")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.show()

# Eigen value centrality analysis
print("Eigen value centralities...")
centrality=nx.eigenvector_centrality_numpy(G)
print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
print( "Max Eigen value : ", max(centrality), "Min Eigen value : ", min(centrality))

# Katz centrality analysis
print("Katz centralities :")
phi = max(centrality)
centrality = nx.katz_centrality(G,1/phi-0.01)
print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
#for n,c in sorted(centrality.items()):
#   print("%d %0.2f"%(n,c))
print( "Avg. katz centrality : ", sum(centrality)/len(centrality), "Max. clustering : ", max(centrality))

degreeCount = collections.Counter(centrality)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Katz Centrality Distribution")
plt.ylabel("Count")
plt.xlabel("Centrality")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.show()

# Clustering analysis
clustering = nx.clustering(G.to_undirected())
print("Clustering coefficients : ", clustering)
print( "Avg. clustering : ", nx.average_clustering(G.to_undirected()), "Max. clustering : ", max(clustering))

degreeCount = collections.Counter(clustering)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.plot(deg, cnt, 'ro-')   
plt.title("Clustering Distribution")
plt.ylabel("Count")
plt.xlabel("Clustering")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.show()