# Shortest Path Between A and B
# https://algo.monster/problems/shortest_path_unweight

# Given an (unweighted) graph, return the length of the shortest path between two nodes A and B, in terms of the
# number of edges.
#
# Input:
# graph: {
#   0: [1, 2],
#   1: [0, 2, 3],
#   2: [0, 1],
#   3: [1]
# }
# A: 0
# B: 3
#
# Output: 2

# Explanation
# BFS is best for finding the distance between two nodes since it traverses level by level. Apply the template from
# BFS template. Since the graph is already built for us, get_neighbors function retrieves the adjacency list.
#
# Time Complexity: O(n+m)
#
# Again we adopt the convention that n denote the number of nodes in the graph and m the number of edges. The time
# spent is equal to the number of nodes and edges in the worst case. Consider for example a linear graph 0->1->2->3
# and so on where we want to get from end to end, we would traverse every node and edge exactly once.
