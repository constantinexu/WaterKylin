# tests/test_core_periphery.py
import networkx as nx
from network_analysis.core_periphery import identify_core_periphery

def test_identify_core_periphery():
    # 创建一个简单的图，其中1, 2, 3是核心节点，4是边缘节点
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3)])
    
    core_nodes, periphery_nodes = identify_core_periphery(G)
    
    assert core_nodes == {1, 2, 3}, "Core nodes identification is incorrect"
    assert periphery_nodes == {4}, "Periphery nodes identification is incorrect"
