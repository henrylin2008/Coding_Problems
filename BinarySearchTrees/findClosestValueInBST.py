# link: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
# Find Closest Value In BST
# You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property
# called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to
# be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node
# to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes
# are either BST nodes themselves or None (null) values. You are also given a target integer value; write a function that
# finds the closest value to that target value contained in the BST. Assume that there will only be one closest value.
# Sample Input:
#             10    , 12
#            /  \
#           5   15
#          / \  / \
#         2  5 13  22
#        /       \
#       1         14
# Sample output: 13

# Method #1: recursively
# Average: O(log(n)) time | O(log(n) space; n in time: number of nodes in BST; n in Space: frames used for call stack
# Worst: O(n) time | O(n) space; tree only have one branch (15 -> 13 -> 10 -> 8 -> 7 -> 5 -> 3 -> 1)
# closest value for comparing with the target value,
def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf")) # call helper method 

def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:  # base case: reach bottom of BST
        return closest
    if abs(target - closest) > abs(target - tree.value): # if closest value is greater than tree.value
        closest = tree.value # set tree.value as the closest value
    if target < tree.value: # if target is < current node value, only explore left side of BST (eliminate right side)
        return findClosestValueInBSTHelper(tree.left, target, closest) # recursive call to left side of the tree
    elif target > tree.value: # if target value is > current node, then explore right side of BST
        return findClosestValueInBSTHelper(tree.right, target, closest) # recursive call to right side of the tree
    else:   # if target = closest, then return closest value
        return closest