from hashmap_tree_intersection import __version__


def test_version():
    assert __version__ == '0.1.0'

import pytest

from hashmap_tree_intersection.hashmap_tree_intersection import findCommon
from hashmap_tree_intersection.hashmap_tree_intersection import *



def test_empty_tree():
    bt = BinaryTree()
    bt1 = BinaryTree()
    actual = findCommon(bt,bt1)
    expect = 'tree is empty'
    assert actual == expect



def test_find_common_1():
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

    assert findCommon(tree1,tree2)=={2, 3, 6, 7}




def test_find_common_2():
    tree1 = BinaryTree()
    tree1.root = Node(10)
    tree1.root.right = Node(20)
    tree1.root.left = Node(30)
    tree1.root.left.left = Node(40)
    tree1.root.left.right = Node(50)
    tree1.root.right.left = Node(60)
    tree1.root.right.right = Node(70)
   


    tree2 = BinaryTree()
    tree2.root = Node(60)
    tree2.root.right = Node(70)
    tree2.root.left = Node(80)
    tree2.root.left.left = Node(90)
    tree2.root.left.right = Node(100)
    tree2.root.right.left = Node(20)
    tree2.root.right.right = Node(30)

    assert findCommon(tree1,tree2)=={20, 30, 60, 70}    