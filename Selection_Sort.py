def SelectionSort(arr):
    for x in range(len(arr)):
        min = x
        temp = arr[x]
        for y in range(x+1, len(arr)):
            if arr[y] < arr[min]:
                min = y                
        arr[x] = arr[min]
        arr[min] = temp
    return arr


print(SelectionSort([1,5,6,3,2,4,150,863,243,2435,0,7]))