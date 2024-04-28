# tests/test_indices.py
import networkx as nx
from network_analysis.indices import calculate_n_pui, calculate_n_pbi

def test_calculate_n_pui():
    # 创建一个图并计算N-PuI
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
    
    # 假设我们已经知道了核心和边缘节点
    core_nodes, periphery_nodes = set([1, 2, 3]), set([4])
    n_pui = calculate_n_pui(G, periphery_nodes)
    
    # 预期的N-PuI值需要根据您的实现来确定
    expected_n_pui = 0  # 请根据实际情况替换为正确的预期值
    assert n_pui == expected_n_pui, "N-PuI calculation is incorrect"

def test_calculate_n_pbi():
    # 创建一个图并计算N-PbI
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
    
    # 假设我们已经知道了核心和边缘节点
    core_nodes, periphery_nodes = set([1, 2, 3]), set([4])
    n_pbi = calculate_n_pbi(G, periphery_nodes)
    
    # 预期的N-PbI值需要根据您的实现来确定
    expected_n_pbi = 1  # 请根据实际情况替换为正确的预期值
    assert n_pbi == expected_n_pbi, "N-PbI calculation is incorrect"
