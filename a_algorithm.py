# -*- coding: utf-8 -*-
"""A* algorithm

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fb_bmm8MLjOHe5NMAK9GAQ3_sSGKYIy-
"""

import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

def heuristic(a, b):
    # Using Manhattan distance as the heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.add(current_node.position)

        # Check if we reached the goal
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Get children (neighbors)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Four possible directions (right, down, left, up)

        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Check if the node is within grid bounds and not an obstacle
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])) and grid[node_position[0]][node_position[1]] == 0:
                if node_position in closed_list:
                    continue  # Already evaluated

                # Create new node
                neighbor_node = Node(node_position, current_node)

                # Calculate costs
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if neighbor is already in the open list
                if any(neighbor_node == node for _, node in open_list if neighbor_node.f < node.f):
                    continue  # This path is not better

                heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

    return None  # No path found

# Example usage
if __name__ == "__main__":
    # Define a simple grid (0 = walkable, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)  # Start position
    goal = (4, 4)   # Goal position

    path = a_star(start, goal, grid)
    print("Path from start to goal:", path)