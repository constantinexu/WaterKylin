# WaterKylin

![1714286033635](https://github.com/constantinexu/WaterKylin/assets/44708925/f49b6215-877b-4dfd-b988-dba81d876fbf)

## Conception
WaterKylin is an open-source Python library designed to provide a comprehensive suite of tools for the analysis of complex networks, with a particular focus on the unique characteristics and roles of peripheral nodes within these networks. In the realm of network science, complex networks are graphs that encapsulate the pairwise interactions within a set of entities—be it social connections, biological interactions, or infrastructure linkages.

At the heart of WaterKylin is the recognition that while much attention has been given to the central or "core" components of networks, the "periphery" plays an equally critical role in determining the network's resilience, adaptability, and overall functionality. Peripheral nodes, although sometimes less connected, serve as the interface with the external environment and are crucial for maintaining the network's response to changes and disturbances.


## Core Features
### Periphery Uniqueness Analysis: 
WaterKylin introduces the Periphery Uniqueness Index (PuI), a metric that quantifies the distinctive attributes of peripheral nodes, setting them apart from their core counterparts.

### Periphery Balance Evaluation: 
With the Periphery Balance Index (PbI), WaterKylin offers insights into how closely the peripheral nodes are integrated with the network's core, affecting the network's equilibrium.

### Modular Design: 
The library is built with a modular architecture, allowing for easy extension and customization to fit various complex network analysis needs.

### Interoperability:
WaterKylin is designed to integrate seamlessly with existing complex network analysis workflows, leveraging popular libraries such as NetworkX.


## Applications

### Ecological Studies:
In ecology, complex networks represent species interactions, and WaterKylin can help in understanding the roles of various species in the ecosystem.
### Social Network Analysis:
It can be used to analyze social networks, identifying influential nodes and the structure of social connections.
### Infrastructure Analysis:
For analyzing transportation or communication networks, WaterKylin can provide insights into the robustness and vulnerability of infrastructure systems.
### Biological Networks: 
In bioinformatics, it can be applied to study gene regulatory networks, protein interaction networks, and more.

## Info
The project is designed and developed by Shipeng Xu, major in ecology and complex networks.
Email: 924225024@qq.com

## Usage

First, clone the WaterKylin repository from GitHub:

```bash
git clone https://github.com/constantienxu/waterkylin.git
cd waterkylin

# Install WaterKylin locally using pip. It's assumed that you have all the necessary dependencies listed in requirements.txt:
pip install .

# Before analyzing a network, you need to prepare your graph data using a compatible library like NetworkX:
import networkx as nx
# Create an empty graph
G = nx.Graph()
# Add nodes and edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# With your graph data ready, use WaterKylin to analyze the periphery:
from waterkylin.core_periphery import identify_core_periphery
from waterkylin.indices import calculate_n_pui, calculate_n_pbi

# Identify core and periphery nodes
core_nodes, periphery_nodes = identify_core_periphery(G)

# Calculate the Periphery Uniqueness Index (N-PuI)
n_pui = calculate_n_pui(G, periphery_nodes)

# Calculate the Periphery Balance Index (N-PbI)
n_pbi = calculate_n_pbi(G, periphery_nodes)



