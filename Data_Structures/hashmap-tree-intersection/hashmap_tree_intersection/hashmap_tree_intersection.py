class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.output = []


    def preOrder(self):
        node = self.root

        def _walk(node):
            self.output.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(node)
        return self.output

    def inOrder(self):
        node = self.root

        def _walk(node):
            if node.left:
                _walk(node.left)
            self.output.append(node.data)
            if node.right:
                _walk(node.right)

        _walk(node)
        return self.output

    def postOrder(self):
        node = self.root

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            self.output.append(node.data)

        _walk(node)
        return self.output

def findCommon(tree1, tree2):
    if tree1.root and tree2.root:
        arr1 = set(tree1.preOrder())
        arr2 = tree2.preOrder()
        output = []
        for i in arr2:
            if i in arr1:
                output.append(i)
        return set(output)
    else:
        return ('tree is empty')

if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.right = Node(2)
    tree1.root.left = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.right.left = Node(6)
    tree1.root.right.right = Node(7)
   


    tree2 = BinaryTree()
    tree2.root = Node(6)
    tree2.root.right = Node(7)
    tree2.root.left = Node(8)
    tree2.root.left.left = Node(9)
    tree2.root.left.right = Node(10)
    tree2.root.right.left = Node(2)
    tree2.root.right.right = Node(3)
   
    print(findCommon(tree1,tree2))