# Tuto funkci implementuj.
def convert_to_matrix(graph):
    matrix = [[0 for x in range(len(graph.keys()))] for y in range(len(graph.keys()))] # Creates Matrix by graph keys

    for i, j in zip(list(graph.values()), graph.keys()): # Loops through graph's keys and values. Note that we can not use graph.items() because of the sorted function below.
        for k in sorted(list(i)): # Loops through sorted list of graph values
            matrix[ord(j.lower()) - 97][ord(k.lower()) - 97] = 1 # Assigns matrix coordinates to 1 for each letter

    return matrix

inputs = [
    {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'C']
    },
    {
        'A': {'F', 'D', 'C'},
        'B': {'F', 'H', 'E', 'C', 'D', 'G'},
        'C': {'A', 'F', 'B', 'D', 'G'},
        'D': {'A', 'F', 'H', 'E', 'B', 'C', 'G'},
        'E': {'F', 'D', 'B', 'G'},
        'F': {'A', 'E', 'B', 'C', 'D', 'G'},
        'G': {'F', 'E', 'B', 'C', 'D'},
        'H': {'B', 'D'}
    },
    {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'D'],
        'D': ['A', 'B', 'C']
    }
]

outputs = [
    [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ],
    [
        [0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0]
    ],
    [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
]
# malá nápověda pro tebe:
# https://graphonline.ru/en/create_graph_by_matrix
# - tady si můžeš nechat vykreslit tvoje grafy

for i, test in enumerate(inputs):
    print(convert_to_matrix(test) == outputs[i])  # True
