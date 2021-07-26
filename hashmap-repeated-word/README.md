# Challenge Summary

## First repeated word

## Whiteboard Process

![cc31](code%20challenge31.png)

## Approach & Efficiency

We have to split the sentence by spaces using split().
We split all the words by spaces and store them in a list.
Use Counter function to count repetition of words
Traverse the list and check if any word has repetition greater than 1
If it is present then print the word and break the loop

**efficiency** 

Time: O(n )
Space: O(n)


## Solution

[Code](hashmap_repeated_word/hashmap_repeated_word.py)

[Tests](tests/test_hashmap_repeated_word.py)