import operator


# 3 ways to visit all the nodes in Tree:
# 1. preorder - root > left > right
# 2. inorder - left > root > right
# 3. postorder - left > right > root


# Pre-Order: root > left > right
# As Function outside of Tree class
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# As method inside of Tree Class
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()


# Post-Order: left > right > root
# As function outside of Tree class
def postorder(tree):
    if tree is not None:  # do nothing if from leaf
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


# Evaluating the left subtree, evaluating the right subtree, and combining them in the root through the function call
# to an operator
def postOrderEval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if tree:
        left = postOrderEval(tree.getLeftChild())
        right = postOrderEval(tree.getRightChild())
        if left and right:  # do if not leaf
            return opers[tree.getRootVal()](left, right)
        else:  # else if it is a leaf, return value
            return tree.getRootVal()


# Inorder: left > root > right
def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


# Returns the expression from the expression tree as a string
def printExp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild()) + ')'
    return sVal
