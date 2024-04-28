# network_analysis/indices.py
import networkx as nx

def calculate_n_pui(G, periphery_nodes):
    """
    Calculate the Network Periphery Uniqueness Index (N-PuI).
    
    Parameters:
    G - A NetworkX graph object.
    periphery_nodes - A collection of nodes identified as periphery nodes.
    
    Returns:
    n_pui - The Network Periphery Uniqueness Index.
    """
    core_degree_avg = nx.degree_histogram(G)[1] / len(list(nx.nodes_with_degree(1, G)))
    n_pui = sum(G.degree(node) - core_degree_avg for node in periphery_nodes) / len(periphery_nodes)
    return n_pui

def calculate_n_pbi(G, periphery_nodes):
    """
    Calculate the Network Periphery Balance Index (N-PbI).
    
    Parameters:
    G - A NetworkX graph object.
    periphery_nodes - A collection of nodes identified as periphery nodes.
    
    Returns:
    n_pbi - The Network Periphery Balance Index.
    """
    shortest_paths = nx.shortest_path_length(G)
    n_pbi = sum(min(shortest_paths[node].get(neigh, float('inf')) for neigh in core_nodes) for node in periphery_nodes) / len(periphery_nodes)
    return n_pbi

