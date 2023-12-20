INF = float('inf')

def floyd_warshall(graph):
    vertices = len(graph)
    distance_matrix = [[INF] * vertices for _ in range(vertices)]
    next_matrix = [[None] * vertices for _ in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                distance_matrix[i][j] = 0
                next_matrix[i][j] = None
            elif graph[i][j] != 0:
                distance_matrix[i][j] = graph[i][j]
                next_matrix[i][j] = j

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                    next_matrix[i][j] = next_matrix[i][k]

    return distance_matrix, next_matrix

# Example usage:
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

distances_matrix, next_matrix = floyd_warshall(graph)

print("Graph adjacency matrix:")
for row in graph:
    print(row)

print("\nShortest distances between all pairs:")
for row in distances_matrix:
    print(row)

print("\nNext vertices in the shortest paths:")
for row in next_matrix:
    print(row)
