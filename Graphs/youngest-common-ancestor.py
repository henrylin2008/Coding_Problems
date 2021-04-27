# Link: https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor
# Youngest Common Ancestor
# Difficulty: Medium

# You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property
# pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree(i.e., the only instance
# that has no ancestor--its ancestor property points to None/null), and the other two inputs are descendants in the
# ancestral tree.
# Write a function that returns the youngest common ancestor to the two descendants.
# Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the youngest common
# ancestor to nodes A and B is node A.

# The youngest common ancestor to nodes A and B is node A.
#       A
#      /
#     B

# Sample Input
# The nodes are from the ancestral tree below.
# topAncestor = node A
# descendantOne = node E
# descendantTwo = node I
#               A
#            /     \
#          B         C
#        /   \      /  \
#       D     E    F    G
#     /  \
#    H    I

# Sample Output
# node B

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# Time: O(d); d: depth of lowest/deepest descendant
# Space: O(1); not storing anything
# Logic: Get the depth of both descendants, comparing the depth of 2 descendants, move the lowest descendant to the same
#        level as the higher descendant; when both descendants are not the same, move the descendant a level above, then
#        return either lower or higher descendant
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:        # (lowerDescendant, higherDescendant, difference)
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:   # depthTwo >= depthOne
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


# get the depth of descendant; the greater value == greater descendant
def getDescendantDepth(descendant, topAncestor):
    depth = 0   # keep track of the depth
    while descendant != topAncestor:
        depth += 1  # increment the depth
        descendant = descendant.ancestor  # going up to the ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    # move the lowerDescendant to the same level as the higher descendant
    while diff > 0:  # until lower descendant at the same level as higher descendant
        lowerDescendant = lowerDescendant.ancestor  # move up the descendant
        diff -= 1    # decrement the diff
    # move up until both descendants are at the same level
    while lowerDescendant != higherDescendant:  # when 2 descendants are not the same, move up until both are the same
        lowerDescendant = lowerDescendant.ancestor  # move up to the ancestor
        higherDescendant = higherDescendant.ancestor    # move up to the ancestor
    return lowerDescendant  # either lowerDescendant or higherDescendant, since both descendants are at the same level
