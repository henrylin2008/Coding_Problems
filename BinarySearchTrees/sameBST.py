# https://www.algoexpert.io/questions/Same%20BSTs
# Same BST
# An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array
# (from left to right) into the BST. Write a function that takes in two arrays of integers and returns a boolean
# representing whether or not these arrays represent the same BST. Note that you are not allowed to construct any BSTs in
# your code. A BST is a Binary Tree that consists only of BST nodes. A node is said to be a BST node if and only if it
# satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less
# than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves
# or None (null) values.

# Method #1: recursive; easiness on reading the code; using array to store
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
    smaller = []  # new array to store every value smaller than first value of the array
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerOrEqual(array): # array to store every value >= array[0]
    biggerOrEqual = [] # new array to store every value that's equal or greater than first value of the array
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual






# Method 2: (Efficient on space), using pointers (instead of array)
# Time: O(n^2); n is number of the nodes in each array;
# Space: O(d); d is the depth of BST tree;

def sameBsts(arrayOne, arrayTwo):
    return areSameBSTs(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))

def areSameBSTs(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1: # if no more root on one array, then no more root on the other array
        return rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]: # if first value of both arrays are not the same, return false
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal) # get the index of first value smaller than the root
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
        # get the index of first value of equal or greater than the root
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxOne, maxVal)

    currentValue = arrayOne[rootIdxOne] # currentValue = current root value
    leftAreSame = areSameBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBSTs(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame # return True when left and right are the same


def getIdxOfFirstSmaller(array, startingIndx, minVal):
    # Find the index of the first smaller value after the startingIdx. Make sure that this value is greater than or equal
    # to the minVal, which is the value of the previous parent node in the BST. If it isn't, then that value is located
    # in the left subtree of the previous parent node.
    for i in range(startingIndx+1, len(array)):
        if array[i] < array[startingIndx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    # Find the index of the first bigger/equal value after the startingIdx,. Make sure that this value is smaller than
    # maxVal, which is the value of the previous parent node in the BST. If it isn't, then that value is located in the
    # right subtree of the previous parent node.
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1
