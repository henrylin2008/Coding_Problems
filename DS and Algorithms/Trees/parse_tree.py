from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator


# 4 rules about Tree Parsing:
# 1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
# 2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator
#    represented by the current token. Add a new node as the right child of the current node and descend to the right
#    child.
# 3. If the current token is a number, set the root value of the current node to the number and return to the parent.
# 4. If the current token is a ')', go to the parent of the current node.

# Recursive:
# Base case: look for both children being a leaf; For leaf, we just return the value
# For other non leaf nodes, we need to perform the operator on the two child subtree values
def buildParseTree(fpexp):
    fplist = fpexp.split()  # create a list by splitting the space
    pStack = Stack()  # create a stack
    eTree = BinaryTree('')  # create a tree
    pStack.push(eTree)  # push the top node
    currentTree = eTree  # current node as node at the top of the tree

    for i in fplist:
        if i == '(':  # if '(': push it down to the left child node
            currentTree.insertLeft('')  # insert a left child
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()  # move it down to the left child node

        elif i in ['+', '-', '*', '/']:  # if it's a operator
            currentTree.setRootVal(i)  # set the root value of the current node to the operator
            currentTree.insertRight('')  # add a new right child
            pStack.push(currentTree)  # add currentTree to the stack
            currentTree = currentTree.getRightChild()  # move to the right child node

        elif i == ')':
            currentTree = pStack.pop()  # go to the parent of the current node

        elif i not in ['+', '-', '*', '/', ')']:  # if it's a number
            try:
                currentTree.setRootVal(int(i))  # set root value of the current node to the number (int(i))
                parent = pStack.pop()  # set the parent
                currentTree = parent  # return to the parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:    # if left child and right child exist
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))    # call function on left child and right child
    else:   # at the leaf node
        return parseTree.getRootVal()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#           *
#        /     \
#      +        3
#    /   \
#   10    5
pt.postorder()
