# merge Sort

Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list.

![mergesort](https://cdn.programiz.com/cdn/farfuture/PRTu8e23Uz212XPrrzN_uqXkVZVY_E0Ta8GZp61-zvw/mtime:1586425911/sites/tutorial2program/files/merge-sort-example_0.png)


# Solution

```
def mergeSort(arr):
    n= len(arr)
    if n > 1:
        mid = int(n/2)
        left = arr[0:mid]
        right = arr[mid:n]
        mergeSort(left)
        mergeSort(right)
        Merge(left, right, arr)
def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=  1
        k =k + 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
```

# Trace

ints: [5, 2, 32, 4, 17, 1, 18, 12]

Split ints into 2 halves: L and R

L [5, 2, 32, 4]
R [17, 1, 18, 12]

Call mergeSort on L, which will continue to split the lists in half until only 1 element remains
[5, 2, 32, 4]
[5, 2,]
[5], [2]

Once the left most pair has been split, stitch back together in order. [5], [2] becomes [2, 5]

Now the same process repeats for the right half of L, not to be confused with R [32, 4] [32], [4] becomes [4, 32]

Stitch L backtogether in order [2, 4, 5, 32]

Repeat the entire process for R [17, 1, 18, 12]

[17, 1, 18, 12]

[17, 1]

[17], [1] becomes [1, 17]

[18, 12]
[18], [12] becomes [12, 18]

Merge R back together in order [1, 12, 17, 18]

Merge L [2, 4, 5, 32] and R [1, 12, 17, 18] to get
[1, 2, 4, 5, 12, 17, 18, 32]


Big(O)

Time: O(nlogn)

Space: O(n)
