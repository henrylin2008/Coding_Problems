# https://www.algoexpert.io/questions/River%20Sizes
# River Sizes
# Difficulty: Medium

# You're given a two-dimensional array(a matrix) of potentially unequal height and width containing only 0s and 1s. Each
# 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either
# horizontally or vertically adjacent(but not diagonally adjacent). The number of adjacent 1s forming a river determine
# its size.
# Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal
# line; it can be L-shaped, for example.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix. The size don't need
# to be in any particular order.

# Sample Input:
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0],
# ]

# Sample Output:
# [1, 2, 2, 2, 5]   // The numbers could be ordered differently.
#
# // The rivers can be clearly seen here:
# // [
# //    [1,  ,  , 1,  ],
# //    [1,  , 1,  ,  ],
# //    [ ,  , 1,  , 1],
# //    [1,  , 1,  , 1],
# //    [1,  , 1, 1,  ],
# // ]


# Time: O(wh); w: width, h: height
# Space: O(wh); w: width, h: height
def riverSizes(matrix):   # main function
    sizes = []   # array to return
    visited = [[False for value in row] for row in matrix]  # set every node to False
    for i in range(len(matrix)):  # iterate through every element in the matrix
        for j in range(len(matrix[i])):
            if visited[i][j]:   # if it's a visited node
                continue    # skip
            traverseNode(i, j, matrix, visited, sizes)  # dealing with unvisited nodes
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]   # stack for DFS to explore neighbor nodes
    # apply DFS
    while len(nodesToExplore):  # while still have nodes to explore
        currentNode = nodesToExplore.pop()  # pop out the final value
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:   # if visited node
            continue        # skip
        visited[i][j] = True    # set as visited
        if matrix[i][j] == 0:   # if it's land, then skip
            continue
        currentRiverSize += 1   # update river size
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)   # get all unvisited neighbor nodes
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)   # add unvisited nodes to nodesToExplore
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)  # add current river size to the sizes array


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:  # neighbor above current row and not visited
        unvisitedNeighbors.append([i - 1, j])   # add it to unvisited neighbors array
    if i < len(matrix) - 1 and not visited[i + 1][j]:   # not at bottom row and not visited
        unvisitedNeighbors.append([i + 1, j])       # add it to unvisited neighbors array
    if j > 0 and not visited[i][j - 1]:     # if not at left most column and not visited neighbor
        unvisitedNeighbors.append([i, j - 1])   # add it to unvisited neighbors array
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:  # if at right most column and not visited neighbor
        unvisitedNeighbors.append([i, j + 1])   # add it to unvisited neighbors array
    return unvisitedNeighbors
