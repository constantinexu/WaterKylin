# network_analysis/core_periphery.py
from networkx import core_number

def identify_core_periphery(G):
    """
    Identify core and periphery nodes in a network using core numbers.
    
    Parameters:
    G - A NetworkX graph object.
    
    Returns:
    core_nodes - A set of nodes identified as core nodes.
    periphery_nodes - A set of nodes identified as periphery nodes.
    """
    core_numbers = core_number(G)
    core_threshold = max(core_numbers.values())
    core_nodes = {node for node, core_num in core_numbers.items() if core_num >= core_threshold}
    periphery_nodes = set(G.nodes()) - core_nodes
    return core_nodes, periphery_nodes
