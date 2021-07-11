# Insertion sort

Insertion sort is the sorting mechanism where the sorted array is built having one item at a time. The array elements are compared with each other sequentially and then arranged simultaneously in some particular order.

To sort an array of size n in ascending order:

1: Iterate from arr[1] to arr[n] over the array. 

2: Compare the current element (key) to its predecessor. 

3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

![insertionsort](https://media.geeksforgeeks.org/wp-content/uploads/insertion_sort-recursion.png)

## Solution

def InsertionSort(arr):
    for i in range (1,len(arr)):
        j=i-1
        temp=arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  
            j = j - 1
            
        arr[j + 1] = temp
    return arr    

**lets take an example**

We have this non-sorted array [5, 2, 32, 4, 17]

Loop from 2nd element i=1 to last element len(ints):

i = 1 [5, (2), 32, 4, 17]

Since 2 is less than 5, move 5 and insert 2 before 5

[2, 5, 32, 4, 17]

i = 2 [2, 5, (32), 4, 17]

Since all elements left of 32 are smaller, 32 doesn't remains where it is

i = 3 [2, 5, 32, (4), 17]

4 moves to index 1 and everything from 5 on moves 1 spot to the right (j + 1)

[2, 4, 5, 32, 17]

i = 4 [2, 4, 5, 32, (17)]

17 will move one spot to the left and 32 gets moved up 1 spot.

[2, 4, 5, 17, 23]

## Big(O)

Time: O(n^2)

Space: O(1)
