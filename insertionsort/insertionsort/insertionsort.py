

def InsertionSort(arr):
    for i in range (1,len(arr)):
        j=i-1
        temp=arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  
            j = j - 1
            
        arr[j + 1] = temp
    return arr    




if __name__ == "__main__":
    arr1 = [8,4,23,42,16,15]
    print('Array => '+f'{arr1}')
    print('Sorted array => '+f'{InsertionSort(arr1)}') 
       
    arr2 = [20,18,12,8,5,-2]
    print('Array => '+f'{arr2}')
    print('Sorted array => '+f'{InsertionSort(arr2)}') 