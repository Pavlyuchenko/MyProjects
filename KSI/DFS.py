class Node:
    def __init__(self, neighbors):
        self.neighbors = neighbors
        self.visited = False

# Tuto funkciu implementuj.
def dfs(graph, node):
    counter = 1
    node.visited = True


    for i in node.neighbors:
        if not graph[i].visited:
            graph[i].visited = True
            counter += dfs(graph, graph[i])

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
    'G': Node([]),
}

sample_graph = {
    1: Node([3, 5, 6, 9]),
    2: Node([4, 6, 8]),
    3: Node([5, 6, 7, 8]),
    4: Node([2, 10]),
    5: Node([1, 3, 7]),
    6: Node([1, 2, 3]),
    7: Node([3, 5]),
    8: Node([2, 3]),
    9: Node([1, 11, 12]),
    10: Node([4]),
    11: Node([9, 12]),
    12: Node([9, 11])
}

tst = {
    1: Node([])
}

print(biggest_component(test_graph_1))  # 5
print(biggest_component(test_graph_2))  # 6
print(biggest_component(sample_graph))  # 12
print(biggest_component(tst))

