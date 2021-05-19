from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


# 4 rules about Tree Parsing:
# 1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
# 2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator
#    represented by the current token. Add a new node as the right child of the current node and descend to the right
#    child.
# 3. If the current token is a number, set the root value of the current node to the number and return to the parent.
# 4. If the current token is a ')', go to the parent of the current node.
def buildParseTree(fpexp):
    fplist = fpexp.split()  # create a list by splitting the space
    pStack = Stack()    # create a stack
    eTree = BinaryTree('')  # create a tree
    pStack.push(eTree)  # push the top node
    currentTree = eTree     # current node as node at the top of the tree

    for i in fplist:
        if i == '(':    # if '(': push it down to the left of the tree
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:  # if it's a operator
            currentTree.setRootVal(i)   #
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()  # go up a level

        elif i not in ['+', '-', '*', '/', ')']:  # if it's a number
            try:
                currentTree.setRootVal(int(i))  #
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#           *
#        /     \
#      +        3
#    /   \
#   10    5
pt.postorder()
