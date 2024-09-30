Optimal node ranking of trees is a crucial concept in various fields, including data science, computer networks, and business analytics. It involves determining the most influential or significant nodes (or elements) within a tree structure, which can represent hierarchical data, decision trees, or even social networks. Here are five brilliant code examples that illustrate optimal node ranking techniques, along with advanced reasoning for their business value.

### File Name
Let's name our file `optimal_node_ranking_trees.py`.

### Code Examples

#### Example 1: PageRank Algorithm for Tree Node Ranking

```python
import numpy as np

def pagerank(adjacency_matrix, damping=0.85, max_iterations=100, tolerance=1.0e-6):
    """
    Calculate the PageRank of nodes in a directed graph represented by an adjacency matrix.

    Parameters:
        adjacency_matrix (np.ndarray): Adjacency matrix of the graph.
        damping (float): Damping factor.
        max_iterations (int): Maximum number of iterations.
        tolerance (float): Tolerance level for convergence.

    Returns:
        np.ndarray: PageRank scores for each node.
    """
    n = adjacency_matrix.shape[0]
    rank = np.ones(n) / n
    for _ in range(max_iterations):
        new_rank = (1 - damping) / n + damping * adjacency_matrix.T.dot(rank)
        if np.linalg.norm(new_rank - rank, 1) < tolerance:
            break
        rank = new_rank
    return rank

# Example usage with a tree structure
adjacency_matrix = np.array([[0, 1, 1, 0],
                              [0, 0, 0, 1],
                              [0, 0, 0, 1],
                              [0, 0, 0, 0]])

rank_scores = pagerank(adjacency_matrix)
print("Node ranks using PageRank:", rank_scores)
```

**Reasoning:** The PageRank algorithm ranks nodes based on their influence in a directed graph. In business applications, this could represent customer relationships in a CRM system or web page importance in SEO. Understanding node influence can help optimize marketing strategies or resource allocation.

---

#### Example 2: Centrality Measures for Node Ranking

```python
import networkx as nx

def calculate_centrality(graph):
    """
    Calculate different centrality measures for nodes in a graph.

    Parameters:
        graph (nx.Graph): A NetworkX graph.

    Returns:
        dict: A dictionary with centrality measures.
    """
    return {
        "degree_centrality": nx.degree_centrality(graph),
        "closeness_centrality": nx.closeness_centrality(graph),
        "betweenness_centrality": nx.betweenness_centrality(graph),
    }

# Example usage
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
G.add_edges_from(edges)

centrality_measures = calculate_centrality(G)
print("Centrality measures:", centrality_measures)
```

**Reasoning:** Centrality measures (degree, closeness, betweenness) provide insights into the importance of nodes within a network. Businesses can use these metrics to identify key players, such as influential customers or critical suppliers, allowing them to focus their engagement strategies effectively.

---

#### Example 3: Depth-First Search (DFS) for Node Ranking Based on Depth

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_rank(node, depth=0, rankings={}):
    """
    Depth-First Search to rank nodes based on their depth.

    Parameters:
        node (TreeNode): The current node in the tree.
        depth (int): Current depth in the tree.
        rankings (dict): Dictionary to store rankings.

    Returns:
        dict: Node rankings based on depth.
    """
    rankings[node.value] = depth
    for child in node.children:
        dfs_rank(child, depth + 1, rankings)
    return rankings

# Example usage
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6)]

depth_rankings = dfs_rank(root)
print("Node rankings based on depth:", depth_rankings)
```

**Reasoning:** This DFS implementation ranks nodes based on their depth in the tree. Businesses can use depth ranking to prioritize customer outreach based on their stage in the customer journey, allowing for targeted marketing efforts and improved customer satisfaction.

---

#### Example 4: Betweenness Centrality for Strategic Decision Making

```python
def betweenness_centrality(graph):
    """
    Calculate betweenness centrality for each node in the graph.

    Parameters:
        graph (nx.Graph): A NetworkX graph.

    Returns:
        dict: A dictionary with betweenness centrality for each node.
    """
    centrality = {node: 0 for node in graph.nodes()}
    for start in graph.nodes():
        for end in graph.nodes():
            if start != end:
                # Shortest paths between start and end
                paths = list(nx.all_shortest_paths(graph, source=start, target=end))
                for path in paths:
                    for node in path[1:-1]:  # Ignore start and end
                        centrality[node] += 1
    return centrality

# Example usage
G = nx.Graph()
edges = [(0, 1), (1, 2), (0, 2), (1, 3), (2, 3)]
G.add_edges_from(edges)

betweenness_scores = betweenness_centrality(G)
print("Betweenness centrality scores:", betweenness_scores)
```

**Reasoning:** Betweenness centrality identifies nodes that act as bridges in a network. In a business context, this can help identify key influencers or decision-makers who connect different departments or markets, facilitating strategic decision-making and collaboration.

---

#### Example 5: Ranking Nodes Based on Revenue Contribution in a Hierarchical Tree

```python
class RevenueNode:
    def __init__(self, value, revenue):
        self.value = value
        self.revenue = revenue
        self.children = []

def revenue_rank(node):
    """
    Rank nodes based on their revenue contributions.

    Parameters:
        node (RevenueNode): The current node in the tree.

    Returns:
        list: Ranked list of nodes based on revenue.
    """
    rankings = []
    
    def recurse(n):
        if n:
            rankings.append((n.value, n.revenue))
            for child in n.children:
                recurse(child)

    recurse(node)
    return sorted(rankings, key=lambda x: x[1], reverse=True)

# Example usage
root = RevenueNode("Company", 100000)
child1 = RevenueNode("Product A", 50000)
child2 = RevenueNode("Product B", 70000)

root.children = [child1, child2]

ranked_revenues = revenue_rank(root)
print("Node rankings based on revenue contributions:", ranked_revenues)
```

**Reasoning:** This example ranks nodes in a hierarchical tree based on their revenue contributions. In a business context, this can help managers prioritize resource allocation, focus on high-performing products, and strategize on underperforming areas to maximize revenue.

---

### Conclusion

These code examples demonstrate various techniques for optimal node ranking in trees, showcasing their real business value. Understanding the importance of nodes can inform decision-making, enhance marketing strategies, and improve overall operational efficiency in various industries. Feel free to test and adapt these examples for your specific use cases!
