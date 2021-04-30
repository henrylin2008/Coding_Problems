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
# Logic: set a sizes array to be the result to return, then set every element in the matrix to False; Go through every
#        element in the matrix; if it's a visited node, the skip it; Use a helper method to deal with unvisited nodes;
#        In the helper method (traverseNode), use DFS to traverse neighbor nodes; while there are still nodes in the
#        nodesToExplore array, pop out the last item from nodesToExplore stack and set it as currentNode (to explore);
#        if currentNode is a visited node or if it's a land, then skip it (no need to explore); set the currentNode as a
#        visited node and increase River size by 1; Use another helper method (unvisitedNeighbors) to get neighbor nodes
#        that are not visited yet, four edges to worry about: 1. upper node that's not on the first row; 2. lower node
#        that's not on the last row; 3. left node that's not on the left most column; 4. right node that's not on the
#        right most column; store any unvisited nodes (unvisitedNeighbors) in an array, then append unvisited it to
#        nodesToExplore array. Lastly, add any river sizes that are > 0 to the final sizes array.
def riverSizes(matrix):   # main function
    sizes = []   # array to return
    visited = [[False for value in row] for row in matrix]  # set every node to False
    for i in range(len(matrix)):  # iterate through every element in the matrix, every row
        for j in range(len(matrix[i])):  # every element in each row
            if visited[i][j]:   # if it's a visited node
                continue    # skip it
            traverseNode(i, j, matrix, visited, sizes)  # dealing with unvisited nodes
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0        # initialize a river size
    nodesToExplore = [[i, j]]   # store neighbor nodes to explore
    # apply DFS, using stack (LIFO) to explore neighbor nodes
    while len(nodesToExplore):  # while there are still nodes to explore
        currentNode = nodesToExplore.pop()  # pop out the last item and set it as currentNode
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:   # if it's visited node, then skip it
            continue
        visited[i][j] = True    # set current node as visited (True)
        if matrix[i][j] == 0:   # if it's land, then skip it
            continue
        currentRiverSize += 1   # update river size
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)   # get all unvisited neighbor nodes
        for neighbor in unvisitedNeighbors:     # add unvisited nodes to nodesToExplore
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)  # add current river size to the sizes array


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:  # neighbor above and above node is not visited
        unvisitedNeighbors.append([i - 1, j])   # add it to unvisited neighbors array
    if i < len(matrix) - 1 and not visited[i + 1][j]:   # not at bottom row and below node is not visited
        unvisitedNeighbors.append([i + 1, j])       # add it to unvisited neighbors array
    if j > 0 and not visited[i][j - 1]:     # if not at left most column and left node is not visited
        unvisitedNeighbors.append([i, j - 1])   # add it to unvisited neighbors array
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:  # if at right most column and right node is not visited
        unvisitedNeighbors.append([i, j + 1])   # add it to unvisited neighbors array
    return unvisitedNeighbors
