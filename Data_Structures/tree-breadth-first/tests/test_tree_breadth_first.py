from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import Node,breadthfirst

def test_version():
    assert __version__ == '0.1.0'


def test_tree_breadth_first_1():
    root = Node(2)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(20)
    assert breadthfirst(root)==[2, 7, 8, 1, 20]





def test_tree_breadth_first_2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
  
    assert breadthfirst(root)==[1,2,3]    





def test_tree_breadth_first_3():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(10)
    assert breadthfirst(root)==[10,20,30,10]    


