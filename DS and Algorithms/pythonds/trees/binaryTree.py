import operator


class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.
    """

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        return (not self.leftChild) and (not self.rightChild)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self, ):
        return self.key

    def inorder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inOrder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printExp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printExp()
            print(')', end=' ')

    def postOrderEval(self):
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        res1 = None
        res2 = None
        if self.leftChild:
            res1 = self.leftChild.postOrderEval()  # // \label{peleft}
        if self.rightChild:
            res2 = self.rightChild.postOrderEval()  # // \label{peright}
        if res1 and res2:
            return opers[self.key](res1, res2)  # // \label{peeval}
        else:
            return self.key


def inOrder(tree):
    if tree is not None:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())


def printExp(tree):
    if tree.leftChild:
        print('(', end=' ')
        printExp(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printExp(tree.getRightChild())
        print(')', end=' ')


def printExp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild()) + ')'
    return sVal


def postOrderEval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postOrderEval(tree.getLeftChild())  # // \label{peleft}
        res2 = postOrderEval(tree.getRightChild())  # // \label{peright}
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)  # // \label{peeval}
        else:
            return tree.getRootVal()


def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))

# t = BinaryTree(7)
# t.insertLeft(3)
# t.insertRight(9)
# inorder(t)
# import operator
# x = BinaryTree('*')
# x.insertLeft('+')
# l = x.getLeftChild()
# l.insertLeft(4)
# l.insertRight(5)
# x.insertRight(7)
# print(printexp(x))
# print(postordereval(x))
# print(height(x))
