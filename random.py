import collections
import matplotlib.pyplot as plt
import networkx as nx

def distr(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Distribution Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.45 for d in deg])
    ax.set_xticklabels(deg)

    plt.show()
    
    degreetuples = zip(deg, cnt)
    
    print("Degree distribution touples (degree, count):" , degreetuples)

print("Degree Distribution Analysis of a Random Network")
    
G = nx.gnp_random_graph(1000, 0.5, seed=None, directed=False)

distr(G)

print("Degree Distribution Analysis of Social network")

G = nx.read_edgelist('facebook_combined.txt',create_using=nx.DiGraph(),nodetype=int)

distr(G)