# WaterKylin 1.0 水麒麟

![1714286033635](https://github.com/constantinexu/WaterKylin/assets/44708925/f49b6215-877b-4dfd-b988-dba81d876fbf)

## Conception
WaterKylin is an open-source Python library designed to provide a new suite of tools for the analysis of complex networks, with a particular focus on the unique characteristics and roles of peripheral nodes within these networks. WaterKylin is the first dedicated complex network analysis tool used for "periphery analysis". In the realm of network science, complex networks are graphs that encapsulate the pairwise interactions within a set of entities—be it social connections, biological interactions, or infrastructure linkages.

At the heart of WaterKylin is the recognition that while much attention has been given to the central or "core" components of networks, the "periphery" plays an equally critical role in determining the network's resilience, adaptability, and overall functionality. Peripheral nodes, although sometimes less connected, serve as the interface with the external environment and are crucial for maintaining the network's response to changes and disturbances.

WaterKylin 是一个开源的 Python 库，旨在提供一套新的复杂网络分析工具，特别关注这些网络中边缘节点的独特特性和作用。WaterKylin是首个用于“边缘分析”的专用复杂网络分析工具。在网络科学领域，复杂网络是包含一组实体之间成对交互的图——无论是社交联系、生物相互作用还是基础设施连接。

WaterKylin 的核心理念是认识到，尽管对网络的中心或核心部分给予了大量关注，但“边缘”在决定网络的弹性、适应性和整体功能方面同样扮演着关键角色。边缘节点虽然有时连接较少，但作为与外部环境的接口，对于维持网络对变化和干扰的响应至关重要。


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



