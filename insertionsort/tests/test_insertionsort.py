from insertionsort import __version__
import insertionsort
from insertionsort.insertionsort import InsertionSort

def test_version():
    assert __version__ == '0.1.0'


def test_insertion_sort1():
    arr=[20,18,12,8,5,-2]
    InsertionSort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]




def test_insertion_sort2():
    arr= [5,12,7,5,5,7]
    InsertionSort(arr)
    assert arr == [5,5,5,7,7,12]




def test_insertion_sort3():
    arr= [2,3,5,7,13,11]
    InsertionSort(arr)
    assert arr == [2,3,5,7,11,13]


        