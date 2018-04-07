# Social Network Analysis Experiments (17MCPC14)

This project contains set of algorithms, examples written to try different approaches to social networking analysis. Most of the code is written using NetworkX python package.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to execute the sample:

git clone https://github.com/17mcpc14/sna.git

### Prerequisites

What things you need to install the software and how to install them

```
Python 3
```
These examples need a minimum version of Python3 as these leverage the object oriented python implementation


```
NetworkX, Matplot, Numpy, Scipy
```
Apart from Python3, the example use NetworkX, Numpy, Scipy and Matplot libraries for network analysis, computation and plotting purposes.


### Installation using Anaconda package manager

A step by step series of examples that tell you have to get a development env running

If you choose to automatically install Python3 and other required libraries using Anaconda or Miniconda, please follow the instruction for corresponding environment setup at https://conda.io/docs/user-guide/install/index.html


```
Running program - Spectral decomposition algorithm for small (34 nodes) Karate Club network
```

1. Open Spyder
2. Open spectral.py
3. Hit run


```
Running program - Spectral decomposition, K-Means algorithm for medium size (1000 nodes) power law cluster graph
```

1. Open Spyder
2. Open spectral_medium.py
3. Hit run

```
Running program - Preferential attachment graphs for degree distribution, Katz centrality, Eigen Value centrality and Clustering coefficients
```

1. Open Spyder
2. Open powergrow.py
3. Hit run


```
Running program - Forest Fire models for degree distribution, Katz centrality, Eigen Value centrality and Clustering coefficients
```

1. Open Spyder
2. Open gn.py
3. Hit run

## Running the programs command line

To execute Spectral decomposition on a small (34 nodes) Karate Club network

1. Run command `python3 spectral.py`

To execute Spectral decomposition, K-Means  on a medium (1000 nodes) power law cluster graph

2. Run command `python3 spectral_medium.py`

To execute Forest Fire models for degree distribution, Katz centrality, Eigen Value centrality and Clustering coefficients

3. Run command `python3 gn.py`

To execute Preferential attachment models for degree distribution, Katz centrality, Eigen Value centrality and Clustering coefficients

4. Run command `python3 powergrow.py`

To execute Degree Distribution Analysis for a Random graph, Social networking graph

4. Run command `python3 random.py`


## Analysis of the experiments

1. The Karate Club network is a fully connected network with low clustering, hence the plotted graph does not clearly give any intuition into Cutset and potential sub graphs

2. The Power Law Cluster graph, as the name indicates, clearly demonstrates clusters and gives a intuitive visibility into potential initial clusters and subsequent clusters

3. Both Eigen Value based Spectral decomposition algorithm as well as K-means algorithm result in very similar but not exactly equal clusters for K >= 2

4. Spectral decomposition takes low computation with GPU based matrix operations while K-means being in iterative algorithm takes slightly more time for K = 2

5. The eigen values and corresponding eigen vectors returned by Spectral decomposition are equal to the number of nodes of the graph G indicating that it is possible to split the graph from k clusters ranging from 1 to the #of nodes.

6. Degree of distribution for a Social network is significantly different from a small world network or from a random network. For a social network, the degree distribution follows a Gamma distribution model while for other networks it follow a Normal distribution

## Authors

* **Prasad Bhavana** - *Initial work* - (https://github.com/17mcpc14)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* NetworkX @ https://networkx.github.io/ for their enormous collection of classes and extensive documentation

* Professor S.Durga Bhavani madam @ http://scis.uohyd.ac.in/People/profile/sdb_profile.php for the inspiration to take up this course and try these beautiful experiments.
