# Trees

Binary Tree and BST Implementation

## Challenge

**Node**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree**

* Create a Binary Tree class


  * Define a method for each of the depth first traversals:


    * pre order
    * in order
    * post order which returns an array of the values, ordered     appropriately.


**Binary Search Tree**


* Create a Binary Search Tree class


  * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:


  * Add


    * Arguments: value
    * Return: nothing
    * Adds a new node with that value in the correct location in the binary search tree.


  * Contains



    * Argument: value
    * Returns: boolean indicating whether or not the value is in the tree at least once.


## Approach & Efficiency


Binary Tree
Order: Time O(n) Space: O(n)
Binary Search Tree
Add: Time O(h) Space: O(1)
Contains: Time O(h) Space O(1)


## API


we have 3 classes :


1. Node class: for creating new nodes that has a value, a right and a lift defined as None


2. Tree class has three methods, pre_order, in_order and post_order:


* pre_order method
* in_order
* post_order


3. Binary Search Tree has 2 methods :


   * Add
   * Contains