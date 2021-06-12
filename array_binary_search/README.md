# Binary search

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## White board

![codechallenge3](code%20challeng3.png)


## Approach and efficiency

I defined a function that takes an array and a value , inside the function called the sort function to sort the array , then iterate over the array and search for that value , if it exists the function returns its index otherwise returns -1.

Time complexity O(n^2)
