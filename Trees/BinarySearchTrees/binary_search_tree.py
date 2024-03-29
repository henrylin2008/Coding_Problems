# Is this a Binary Search Tree?
# Write a function that takes a binary tree and returns true if it is a binary search tree, and false if not.
# ex:
# head1 =   0
#         /   \
#        1     2
#       / \   / \
#      3  4  5   6
# head1 is NOT a binary search tree.

# head2 =      3
#            /   \
#           1     4
#          /  \  /  \
#         0   2  5   6
# head2 is Not a binary search tree

# head3  =     3
#            /    \
#          1       5
#         /  \    /  \
#        0   2   4    6
# head3 is a binary search tree

# head4  =      3
#             /    \
#            1      5
#           / \
#          0   4
# head4 is NOT a binary search tree


# Use this class to create binary trees.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# Main function to validate a BST
def is_bst(node, lower_limit=None, upper_limit=None):
    # base case: lower_limit < current_node.value < upper_limit
    if lower_limit is not None and node.value < lower_limit:  # if lower_limit exist and current node < lower_limit
        return False
    if upper_limit is not None and upper_limit < node.value:  # if upper_limit exist and upper_limit < current node
        return False

    is_left_bst = True      # True if left sub-tree is a BST
    is_right_bst = True     # True if right sub-tree is a BST
    if node.left:           # if left subtree node exist, recursive call is_bst on subtree left node
        # node.left: left subtree node; lower_limit same as current lower_limit; node.value: upper limit
        is_left_bst = is_bst(node.left, lower_limit, node.value)    # recursive call to check left subtree node
    if is_left_bst and node.right:  # if left bst is true and node.right exist; recursive call is_bst on sub right node
        is_right_bst = is_bst(node.right, node.value, upper_limit)  # recursive call to check right subtree node
    # print("bst:", is_left_bst and is_right_bst)
    return is_left_bst and is_right_bst


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head node
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping0 = {0: [1, 2]}
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
head0 = create_tree(mapping0, 0)
# This tree is:
#  head0 = 0
#        /   \
#       1     2
head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

# is_bst(head0)  # should return False
# is_bst(head1)  # should return False
# is_bst(head2)  # should return False
is_bst(head3)  # should return True
# is_bst(head4)  # should return False
