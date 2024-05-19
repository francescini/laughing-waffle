pip install matplotlib networkx

import matplotlib.pyplot as plt
import networkx as nx

def create_control_diagram():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes with labels
    nodes = {
        'UI': 'User Interface',
        'IP': 'Input Processing',
        'LM': 'Language Model (Core)',
        'OP': 'Output Processing',
        'FD': 'Feedback System',
        'DM': 'Data Management',
        'SEC': 'Security Systems',
        'RC': 'Regulatory Compliance',
        'MU': 'Maintenance & Updates'
    }
    for node, label in nodes.items():
        G.add_node(node, label=label)

    # Add edges between nodes
    edges = [
        ('UI', 'IP', 'User Input'),
        ('IP', 'LM', 'Processed Input'),
        ('LM', 'OP', 'Generated Response'),
        ('OP', 'UI', 'Formatted Response'),
        ('UI', 'FD', 'User Feedback'),
        ('FD', 'LM', 'Feedback Analysis & Improvements'),
        ('DM', 'LM', 'Data Access'),
        ('SEC', 'DM', 'Security Enforcement'),
        ('RC', 'UI', 'Compliance Checks'),
        ('MU', 'LM', 'Updates & Patches'),
        ('MU', 'DM', 'Data System Updates'),
        ('MU', 'SEC', 'Security Updates'),
        ('RC', 'SEC', 'Legal Requirements for Security'),
        ('RC', 'DM', 'Data Compliance Standards')
    ]
    for start, end, label in edges:
        G.add_edge(start, end, label=label)

    # Use a layout to position nodes
    pos = nx.spring_layout(G)  # Positions nodes using Fruchterman-Reingold force-directed algorithm

    # Draw nodes, edges, and labels
    nx.draw(G, pos, with_labels=True, node_size=7000, node_color='skyblue', font_size=9, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    # Show the graph
    plt.title('LLM Control Structure Diagram')
    plt.show()

create_control_diagram()
