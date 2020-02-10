'''
Use low and high pointers 
base case of low and high not overlapping
check for value at mid pos
check size at mid and change high and low accordingly 
'''


def BinarySearch(array, value):
    low = 0 
    high = len(array) - 1
    while (low <= high):
        mid = (low + high) //2 
        print(low)
        if array[mid] == value:
            return mid
        if array[mid] < value:
            low = mid+1
        if array[mid] > value:
            high = mid - 1      
    return -1 

array = [1,2,3,4,5,6,7,8,9]
print(BinarySearch(array, 10))
