# -*- coding: utf-8 -*-
"""map colouring

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lZbk10gmfMa-9C95mG3T9PF33oWs1PbK
"""

class MapColoring:
    def __init__(self, num_colors, adjacency_matrix):
        self.num_colors = num_colors
        self.adjacency_matrix = adjacency_matrix
        self.num_nodes = len(adjacency_matrix)
        self.colors = [-1] * self.num_nodes

    def is_valid(self, node, color):
        for neighbor in range(self.num_nodes):
            if self.adjacency_matrix[node][neighbor] == 1 and self.colors[neighbor] == color:
                return False
        return True

    def solve(self):
        if self.color_map(0):
            return self.colors
        else:
            return None

    def color_map(self, node):
        if node == self.num_nodes:
            return True

        for color in range(self.num_colors):
            if self.is_valid(node, color):
                self.colors[node] = color
                if self.color_map(node + 1):
                    return True
                self.colors[node] = -1  # Backtrack

        return False

def print_solution(colors):
    if colors is None:
        print("No solution exists")
    else:
        print("Solution exists: ")
        for idx, color in enumerate(colors):
            print(f"Node {idx}: Color {color}")

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix for a graph
    # 0 - no connection, 1 - connected
    adjacency_matrix = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]

    # Number of colors to be used
    num_colors = 3

    map_coloring = MapColoring(num_colors, adjacency_matrix)
    solution = map_coloring.solve()
    print_solution(solution)