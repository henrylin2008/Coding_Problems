# Visible Tree Node | Number of Visible Nodes

# In a binary tree, we define a node "visible" when no node on the root-to-itself path (inclusive) has a greater
# value. The root is always "visible" since there are no other nodes between the root and itself. Given a binary
# tree, count the number of "visible" nodes.
#
# Input:
#               5
#             /    \
#            4      6
#           / \
#         3    8
#
#       Visible nodes: 5, 6, 8
# Output: 3
#
# For example: Node 4 is not visible since 5>4, similarly Node 3 is not visible since both 5>3 and 4>3. Node 8 is
# visible since all 5<=8, 4<=8, and 8<=8.
