import networkx as nx
import matplotlib.pyplot as plt
import time
watts_strogatz = nx.watts_strogatz_graph(20,4,0)
nx.draw_circular(watts_strogatz)
plt.show()

fig = plt.figure()

p = 0
for i in range(100):
    p = p + (1/100) 
    watts_strogatz = nx.watts_strogatz_graph(20,4,p)
    nx.draw_circular(watts_strogatz)
    time.sleep(1)
    fig.canvas.draw()
    