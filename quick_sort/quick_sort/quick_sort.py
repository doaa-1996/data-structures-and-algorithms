def partition(arr,low,high): 
    i = ( low-1 )       
    pivot = arr[high]
    for j in range(low , high): 

        if   arr[j] < pivot: 
        
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
   
def quicksort(arr,low,high): 
    if low < high: 
        p = partition(arr,low,high) 
  
        quicksort(arr, low, p-1) 
        quicksort(arr, p+1, high) 

if __name__ == "__main__":
    arr = [8, 4, 3, 7, 1, 9]
    print('The original array :'+f'{arr}')
    n = len(arr)
    quicksort(arr, 0, n-1)
    print('The sorted array'+f'{arr}')