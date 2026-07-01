def bubble_sort(listt):
    for i in range(len(listt)):
        for i in range(len(listt) - 1):

            x = listt[i]
            y = listt[i + 1]

            if x > y:
                listt[i], listt[i + 1] = listt[i + 1], listt[i]
    return listt

def selection_sort(listt):
    for i in range(len(listt)):
        min_index = i
        for x in range(i + 1, len(listt)):
            if listt[x] < listt[min_index]:
                min_index = x
        listt[i], listt[min_index] = listt[min_index], listt[i]
    return listt

def insertion_sort(listt):
    for i in range(1, len(listt)):
        value = listt[i]
        x = i - 1

        while x >= 0 and value < listt[x]:
            listt[x + 1] = listt[x]
            x -= 1

        listt[x + 1] = value

    return listt

def partition(array, low, high):  
    pivot = array[high]           
    i = low - 1                   

    for j in range(low, high):    
        if array[j] <= pivot:     
            i += 1                
            array[i], array[j] = array[j], array[i]  

    array[i+1], array[high] = array[high], array[i+1]  
    return i+1                   


def quick_sort(array, low=0, high=None):  
    if high is None:                    
        high = len(array) - 1           

    if low < high:                       
        pivot_index = partition(array, low, high)  
        
        quick_sort(array, low, pivot_index-1)     
        quick_sort(array, pivot_index+1, high)      