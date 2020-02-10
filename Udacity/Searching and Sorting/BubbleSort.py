'''
swapping is the main loop (j)
each j loop bubbles the largest value 
hence, the j loop must be rerun until all the values bubble up 
i loop tracks the number of times the bubbling takes place

'''



def Bubble(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [9,7,6,5,4,3,2,1]
Bubble(array)
print(array)                    