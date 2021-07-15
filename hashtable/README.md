# Hashtables

[Code](hashtable/hashtable.py)

[Tests](tests/test_hashtable.py)


## Challenge

The code challenge was to create a hash table. The approach I used was to create a list of linked lists. You have the option to set the length of the base list in the init function (default: 1024). The spaces are set to None until a value is inserted at that point. At that point a linked list is created at that index. The linked lists have the same functionality as the hash table of add contains and get.

## Approach & Efficiency

Add:

Time: O(1)

Space: O(1)


Contains:

Time: O(1)

Space: O(1)


Get:

Time: O(1)

Space: O(1)


Hash:

Time: O(1)

Space: O(1)




## API

Add:

In: (Key, Value)

Out: None


Contains:

In:Key

Out:True/False


Get:

In: Key

Out: Value


Hash:

In: Key Int or String

Out: Index Int of position in List