The Four Color Theorem states that every planar map can be colored with no more than four colors such that no two adjacent regions (areas sharing a common boundary) have the same color. The proof of this theorem involves two main components: **Discharging** and **Reducibility**. Below are two code examples that illustrate these concepts programmatically, with applications to map coloring, following the same robust format as previous examples.

### 1. Discharging Method for Planar Graph Coloring

**Description**: 
The discharging method is a technique used to prove properties of planar graphs by distributing "charges" across the graph and applying rules to redistribute those charges. In the context of the Four Color Theorem, discharging is used to handle vertices and regions with different degrees and ensure that the overall graph can be colored with four colors.

#### Python Code Example:
```python
import networkx as nx
import matplotlib.pyplot as plt

def apply_discharging(graph):
    """Discharging method for planar graph coloring."""
    charges = {node: degree for node, degree in dict(graph.degree()).items()}
    
    # Discharging rules: redistribute charges from higher-degree nodes to lower-degree ones
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        if charges[node] > 5:  # Arbitrary threshold to trigger discharging
            charge_per_neighbor = (charges[node] - 5) / len(neighbors)
            charges[node] = 5  # Limit charge to 5
            for neighbor in neighbors:
                charges[neighbor] += charge_per_neighbor
    
    return charges

# Example usage on a planar graph
G = nx.random_geometric_graph(20, 0.3)
charges = apply_discharging(G)

# Visualize graph with charges
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=700, node_color=[charges[node] for node in G.nodes()], cmap=plt.cm.Wistia)
plt.title("Planar Graph with Discharging Method Applied")
plt.show()
```

### Value:
- **Planar Graph Validation**: The discharging method is used to validate whether a planar graph can be colored with four colors by ensuring that no vertex has excess "charge" and conflicts are avoided.

---

### 2. Reducibility in Planar Graph Coloring

**Description**: 
The concept of reducibility is used to simplify complex planar graphs into smaller, more manageable subgraphs that are easier to color. A reducible configuration means that any planar graph containing that configuration can be reduced while maintaining the four-colorability.

#### Python Code Example:
```python
def is_reducible(graph):
    """Check if a planar graph contains reducible configurations."""
    for node in graph.nodes():
        degree = graph.degree(node)
        if degree <= 5:
            return True  # A node with degree <= 5 is a reducible configuration
    return False

def color_planar_graph(graph):
    """Color a planar graph using reducibility and a greedy coloring algorithm."""
    if not nx.check_planarity(graph)[0]:
        raise ValueError("The graph is not planar")

    while is_reducible(graph):
        # Greedy coloring on reducible subgraphs
        color_map = nx.coloring.greedy_color(graph, strategy="largest_first")
        
        # Remove a node with a reducible configuration and repeat
        reducible_nodes = [node for node in graph.nodes() if graph.degree(node) <= 5]
        if reducible_nodes:
            graph.remove_node(reducible_nodes[0])

    return color_map

# Example usage on a planar graph
G = nx.random_geometric_graph(20, 0.25)
coloring = color_planar_graph(G)
print("Coloring of the Planar Graph:", coloring)

# Visualize colored graph
plt.figure(figsize=(8, 8))
nx.draw(G, node_color=[coloring[node] for node in G.nodes()], with_labels=True, cmap=plt.cm.Set3)
plt.title("Planar Graph Colored Using Reducibility Method")
plt.show()
```

### Value:
- **Graph Reduction for Simplification**: The reducibility method breaks down the graph into simpler subgraphs that are easier to color using a greedy coloring algorithm. This is essential for complex planar graphs where manual coloring would be infeasible.

---

### Combined Conclusion

Both **discharging** and **reducibility** are critical techniques used to ensure that a planar map (or graph) can be colored with no more than four colors. Discharging deals with redistributing degrees (charges) among nodes, while reducibility breaks down a graph into simpler configurations that can be handled through coloring algorithms.

### Suggested File Name

A suitable file name for this collection could be:

**`planar_graph_four_color_theorem_discharging_reducibility.py`**

This file name captures both the discharging and reducibility techniques involved in the Four Color Theorem, making it clear that the code examples focus on different aspects of planar graph coloring.
