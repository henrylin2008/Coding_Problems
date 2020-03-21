# https://www.algoexpert.io/questions/Same%20BSTs
# Same BST
# An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array
# (from left to right) into the BST. Write a function that takes in two arrays of integers and returns a boolean
# representing whether or not these arrays represent the same BST. Note that you are not allowed to construct any BSTs in
# your code. A BST is a Binary Tree that consists only of BST nodes. A node is said to be a BST node if and only if it
# satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less
# than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves
# or None (null) values.

# Method #1: recursive; easiness on reading the code
# Time: O(n^2); n is the number of nodes in each array
# Space: O(n^2); n is the number of nodes in each array
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo): # False if both arrays don't have same length
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0: # True when array reaches to the end
        return True

    if arrayOne[0] != arrayTwo[0]: # first element of 2 arrays must be the same (according to description)
        return False

    # O(4N) and n times ==> O(n^2) time; same thing for space complexity
    leftOne = getSmaller(arrayOne) # left subtree of arrayOne, anything < root
    leftTwo = getSmaller(arrayTwo) # left subtree of arrayTwo
    rightOne = getBiggerOrEqual(arrayOne) # right subtree of arrayOne, anything >= root
    rightTwo = getBiggerOrEqual(arrayTwo) # right subtree of arrayTwo

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo) # return True only if subtrees of left and right
                                            # are the same

def getSmaller(array): # array to store every value < array[0]
    smaller = []  # new array
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerOrEqual(array): # array to store every value >= array[0]
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual






# Method 2: (Efficient on space), using pointers (instead of array)
# Time: O(n^2); n is number of the nodes in each array;
# Space: O(d); d is the depth of BST tree;

def sameBsts(arrayOne, arrayTwo):
    return areSameBSTs(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, float('-inf'), float('inf'))

def areSameBSTs(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxOne, maxVal)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBSTs(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIndx, minVal):
    for i in range(startingIndx+1, len(array)):
        if array[i] < array[startingIndx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1
