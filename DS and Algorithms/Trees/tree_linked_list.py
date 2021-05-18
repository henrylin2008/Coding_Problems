# Implementing tree with a linked list
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:  # no existing left child
            self.leftChild = BinaryTree(newNode)  # add a node to the tree
        else:  # if there's left child, we insert a node and push the existing child down one level in the tree.
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # following methods are for the assignment from the section
    # Write a function buildTree that returns a tree using the nodes and references implementation that looks like th
    def printTree(self, level=0):  # outline of the tree
        print(" " * level, self.key)
        if self.leftChild is not None:
            self.leftChild.printTree(level + 1)
        else:
            print(" " * (level + 1), "None")
        if self.rightChild is not None:
            self.rightChild.printTree(level + 1)
        else:
            print(" " * (level + 1), "None")

    def depth(self, d=0):
        """Get the depth of the tree"""
        d1 = 0
        d2 = 0
        if self.leftChild:
            d1 = max(self.leftChild.depth(d + 1), d)
        if self.rightChild:
            d2 = max(self.rightChild.depth(d + 1), d)
        return max(d1, d2, d)

    def _toArray(self, left, i, right, s):
        """convert a tree to array"""
        left += 1
        i = i * 2 + right
        s[left - 1][i] = self.key
        if self.leftChild:
            self.leftChild._toArray(left, i, 0, s)
        if self.rightChild:
            self.rightChild._toArray(left, i, 1, s)

    def diagram(self):
        content_size = 4
        space = " "
        bottom_size = (content_size + len(space))
        depth = self.depth()
        if depth > 4:
            print("depth is too large")
            return
        width = 5 * 2**depth
        s = list()
        for i in range(depth + 1):
            s.append([""] * (2 ** i))
        self._toArray(0, 0, 0, s)
        for l in range(depth + 1):
            for i in range(len(s[l])):
                print(str(s[l][i]).center(width // 2 ** l), end="")
            print()
            if l < depth:
                for i in range(len(s[l])):
                    print("/   \\".center(width // 2 ** l), end="")
                print()


def main():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    r.insertRight('f')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.diagram()


if __name__ == "__main__":
    main()

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
