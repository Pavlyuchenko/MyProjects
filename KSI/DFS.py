class Node:
    def __init__(self, neighbors):
        self.neighbors = neighbors
        self.visited = False

# Tuto funkciu implementuj.
def dfs(graph, node):
    counter = 0

    for i in node.neighbors:
        if not graph[i].visited:
            graph[i].visited = True
            counter += 1
            counter += dfs(graph, graph[i])

    node.visited = True

    return counter


# Tuto funkciu implementuj.
def biggest_component(graph):
    maxim = 0

    for i in graph.values():
        if not i.visited:
            maxim = max(dfs(graph, i), maxim)

    return maxim


# Testy

test_graph_1 = {
    'A': Node(['B', 'C']),
    'B': Node(['A', 'C', 'E', 'G']),
    'C': Node(['A', 'B', 'E']),
    'D': Node(['F', 'I', 'J']),
    'E': Node(['B', 'C']),
    'F': Node(['D', 'I', 'J']),
    'G': Node(['B']),
    'H': Node(['K']),
    'I': Node(['D', 'F']),
    'J': Node(['D', 'F']),
    'K': Node(['H'])
}

test_graph_2 = {
    'A': Node(['B', 'C', 'D']),
    'B': Node(['A', 'C']),
    'C': Node(['A', 'B']),
    'D': Node(['A', 'E', 'F']),
    'E': Node(['D', 'F']),
    'F': Node(['D', 'E']),
    'G': Node([])
}


print(biggest_component(test_graph_1))  # 5
print(biggest_component(test_graph_2))  # 6

