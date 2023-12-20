INF = float('inf')

def floyd_warshall(graph):
    vertices = len(graph)
    
    # Initialize the distance matrix with direct edge weights
    distance_matrix = [[INF] * vertices for _ in range(vertices)]
    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                distance_matrix[i][j] = 0
            elif graph[i][j] != 0:
                distance_matrix[i][j] = graph[i][j]
    
    # Update the distance matrix using all possible intermediate vertices
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    return distance_matrix

# Example usage:
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result_matrix = floyd_warshall(graph)

# Print the result matrix
print("Shortest distances between all pairs:")
for row in result_matrix:
    print(row)
