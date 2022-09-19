# Minimum Cost to Visit Every Node in a Graph
# https://algo.monster/problems/min_cost_to_visit_every_node

# Output the minimum cost to traverse every node in a directed weighted graph. The graph will be in the form of a 2D
# list where element [i,j] in the array denotes the weight of the directed edge from i to j. If the value is 0 then
# the edge doesn't exist. You do not have to end at the starting node. All edges are guaranteed to be in the range [
# 0,1000], there will not exceed 15 nodes in the graph. The starting node will always be at node 0. If a solution
# does not exist return -1.

# Solution
# Maintain a bitmask for the nodes that you visited. We can then perform dfs to check nodes we have not visited and
# record the minimum value and return that for our recursive function. For further reading, this problem is actually
# quite famous and known as the Travelling Salesman Problem(https://en.wikipedia.org/wiki/Travelling_salesman_problem).
#
# Time Complexity: O(2^n)
#
# Bitmask problems tend to reduce O(n!) time complexity or worse to O(2^n)

from typing import List


def min_cost_to_visit_every_node(graph: List[List[int]]) -> int:
    # set dp array size equal to 2^(number of nodes)
    dp = [[0] * len(graph) for _ in range(1 << len(graph))]

    def f(bitmask, cur):
        # check if we have visited every node
        if bitmask == (1 << len(graph)) - 1: return 0
        if dp[bitmask][cur] != 0: return dp[bitmask][cur]
        # set to arbitrary large value, edges are only 1000 and 15 nodes so total can never reach 0x3f3f3f3f
        ans = 0x3f3f3f3f
        # loop through all the neighbours for this particular node
        for i in range(len(graph[cur])):
            if (bitmask & (1 << i)) == 0 and graph[cur][i] != 0:
                # if we have not visited this node, call the recursive function and see if we get a new minimum
                ans = min(ans, graph[cur][i] + f((bitmask | (1 << i)), i))
        dp[bitmask][cur] = ans
        return ans

    # set node 0 as visited and start at node 0
    ans = f(1, 0)
    return -1 if ans == 0x3f3f3f3f else ans


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_cost_to_visit_every_node(graph)
    print(res)
