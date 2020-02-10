'''

Split the array into left and right 
recursively call the splitting until we get individual splits 
sort the individual splits while merging --> (compare and copy the lowest into the array)

'''
def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1    
        # When one of the lists still have elements left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        print(array)

array = [77, 5, 2, 76, 22, 98]
MergeSort(array)
print(array)