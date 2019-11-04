def mergeArrays(arr1, arr2, m, n): 
    arr3 = [None] * (m + n) 
    i = 0
    j = 0
    k = 0
  
    while i < m and j < n: 
      
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
      
    while i < m: 
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < n: 
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    print("Array after merging: ") 
    for i in range(m + n): 
        print(str(arr3[i]), end = " ") 
  

arr1 = [1, 3, 5, 7, 9] 
n1 = len(arr1) 
  
arr2 = [4, 6, 8] 
n2 = len(arr2) 

mergeArrays(arr1, arr2, n1, n2)
