class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 
def breadthfirst(root):
    if root is None:
        return
     
    queue = []
 
    queue.append(root)
    arr=[]
    while(len(queue) > 0):
        arr.append(queue[0].data)
        node = queue.pop(0)
 
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)
    return arr      
 
root = Node(5)
root.left = Node(9)
root.right = Node(3)
root.left.left = Node(2)
root.left.right = Node(20)
 
print ("values in the tree")
print(breadthfirst(root))
