#Detta är en programbibliotek för sorterings algoritmer
#Vi inleder med att importera random for bogosort
import random


class API:
    
    def __init__(self):
        pass
    
    #tillämpning av counting sort
    def counting_sort(self,array_to_be_sorted):
        if array_to_be_sorted == []:
            return False
        if isinstance(array_to_be_sorted, list):        
            #k representerar den största elementet i den inmatade arrayen.
            k = max(array_to_be_sorted)
            store_count_array = [0] * (k+1) #Skapar en array för att kunna lagra count
            for i in range(0, len(array_to_be_sorted)):
                store_count_array[array_to_be_sorted[i]] += 1
            #modifierar store_count_array beroende på multiplar
            for i in range(0, len(store_count_array)-1):
                store_count_array[i+1] = store_count_array[i+1] + store_count_array[i]
            #skapar en ny array med ekvivalent index som den inmatade arrayen
            sorted_array = [0] * (len(array_to_be_sorted))

            #sorting the array for loopen sorterar output arrayen
            #den inleder med att kolla värdet av den inmatade arrayen
            #detta ger oss indexeringen av store_count_array

            for i in range(0, len(sorted_array)):
                sorted_array[store_count_array[array_to_be_sorted[i]]-1] = array_to_be_sorted[i]
                store_count_array[array_to_be_sorted[i]] -= 1 
            return sorted_array
        
        else:
            return False

    def sort_duplicates(self,array):
        if array == []:
            return False
        if isinstance(array, list):        

                #Creating a dictionary
                array_dict = dict()
                
                #Putting in unique values of array into the dictionary
                #We are looping through array therefore we have a time complexity of O(n)
                for i in array:
                    array_dict[i] = array_dict.get(i, 0) + 1
                    
                #We wish to sort dictionary, this has time complexity of Ordo(k log k)
                sorted_dict = sorted(array_dict)
                
                #We create a new array
                sorted_array = [0] * len(array)

                #With the help of our sorted list and dictionary we sort the input array
                i = 0
                for key in sorted_dict:
                    for value in range(0, array_dict[key]):
                        sorted_array[i] = key
                        i = i + 1

                return sorted_array
        else:
            return False
    
    #Implementation of bubblesort
    def bubblesort(self,array):
        if array == []:
            return False
        if isinstance(array, list):        

            #We loop through the length of the array
            for j in range(len(array)-1,0,-1):
                #This loop is dependent on the previous for-loop
                for i in range(0, j):
                    #By comparing the n element with n+1 element in the array
                    #We switch the index of the elements if n > n+1
                    #Therefore obtaining bubblesort
                    if (array[i] > array[i+1]):
                        value_next = array[i+1]
                        array[i+1] = array[i]
                        array[i] = value_next
                        
            return array
        else:
            return False

    #This is a help function to check if the input array is sorted
    def is_list_sorted(self,array):
        #We check if the neighbor element n+1 is less than n
        for i in range(0,len(array)-1):
            if array[i] > array[i+1]:
                #If this is false then return False
                return False
        #If this is true then it returns True because the array is sorted
        return True

    #Implementation of bogosort
    def bogosort(self,array):
        if array == []:
            return False
        if isinstance(array, list): 
            #We keep randomizing the array until it is sorted
            while self.is_list_sorted(array) == False:
                random.shuffle(array)
                
            return array
        else:
            return False

    #Implementation of insertion sort
    def insertion_sort(self, array):
        if array == []:
            return False
        if isinstance(array, list):
            #Looping through the whole list
            for i in range(0, len(array)-1):
                #Creating smaller list to sort
                if array[i+1] < array[i]:
                    save = array[i+1]
                    for j in range(i,-1,-1):
                        if array[j+1] < array[j]:
                            array[j+1] = array[j]
                            array[j] = save

            return array
        else:
            return False
    
    def quicksort(self, array):
        if array == []:
            return False
        if isinstance(array, list): 
            length = len(array)
            pivot = array[length-1]
            variable_less = -1
            #Begin by sorting the list with respect to the pivot
            for i in range(0,length):
                
                if array[i] <= pivot:
                    variable_less = variable_less + 1
                    swap = array[variable_less]
                    array[variable_less] = array[i]
                    array[i] = swap
            #checking if list is sorted, continue till list is sorted
            if self.is_list_sorted(array) == True:
                return array
            else:
                #creating two sub problems through recurrence and continue sorting thro new pivot
                return self.quicksort(array[:variable_less])+self.quicksort(array[variable_less:])           
        else:
            return False
        
    def shellsort(self,arr):
        if arr == []:
            return False
        
        if isinstance(arr, list):
            #J equals a gap between between elements in the array
            #When J reaches 1 bubblesort is applied
            j = len(arr)//2
            #Looping till j is equal to 1 to call bubblesort
            #Replacing elements in respect to the gap

            while j != 1:
                for i in range(j):
                    if arr[j] < arr[i]:
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                j = j//2
            if j == 1:
                #calling bubblesort
                arr = self.bubblesort(arr)
            return arr
        else:
            return False
                        
                    

    
    

def main():
    sort = API()
    #Counting sort hanterar enbart arrayer med heltal => 0
    #Tester för Counting sort
    assert sort.counting_sort(1) == False
    assert sort.counting_sort([]) == False
    assert sort.counting_sort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.counting_sort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.counting_sort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.counting_sort([1,2,3,4]) == [1,2,3,4]

    #Tester för sortingerings algoritmen som sorterar dupletter, sort_duplicates
    assert sort.sort_duplicates(1) == False
    assert sort.sort_duplicates([]) == False
    assert sort.sort_duplicates([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.sort_duplicates([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.sort_duplicates([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.sort_duplicates([1,2,3,4]) == [1,2,3,4]


    assert sort.sort_duplicates([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.sort_duplicates([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.sort_duplicates([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]
    
    #Tester för bubble sort
    assert sort.bubblesort(1) == False
    assert sort.bubblesort([]) == False
    assert sort.bubblesort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.bubblesort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.bubblesort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.bubblesort([1,2,3,4]) == [1,2,3,4]


    assert sort.bubblesort([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.bubblesort([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.bubblesort([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]

    #Tester för bogo sort
    assert sort.bogosort(1) == False
    assert sort.bogosort([]) == False
    assert sort.bogosort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.bogosort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.bogosort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.bogosort([1,2,3,4]) == [1,2,3,4]


    assert sort.bogosort([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.bogosort([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.bogosort([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]

    #Tester för Insertion sort 
    
    #print(sort.insertion_sort([9,100,32,43,546,10,2,3]))
    assert sort.insertion_sort(1) == False
    assert sort.insertion_sort([]) == False
    assert sort.insertion_sort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.insertion_sort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.insertion_sort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.insertion_sort([1,2,3,4]) == [1,2,3,4]


    assert sort.insertion_sort([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.insertion_sort([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.insertion_sort([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]

    
    #Tester för Quick sort
    assert sort.quicksort(1) == False
    assert sort.quicksort([]) == False
    assert sort.quicksort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.quicksort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.quicksort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.quicksort([1,2,3,4]) == [1,2,3,4]


    assert sort.quicksort([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.quicksort([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.quicksort([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]

    assert sort.shellsort(1) == False
    assert sort.shellsort([]) == False
    assert sort.shellsort([3,2,1,4,5,6]) == [1,2,3,4,5,6]
    assert sort.shellsort([9,100,32,43,546,10,2,3]) == [2,3,9,10,32,43,100,546]
    assert sort.shellsort([2392,43092,239103,3242]) == [2392,3242,43092,239103]
    assert sort.shellsort([1,2,3,4]) == [1,2,3,4]


    assert sort.shellsort([-1,-1,2,1]) == [-1,-1,1,2]
    assert sort.shellsort([-1,-1,-22,1]) == [-22,-1,-1,1]
    assert sort.shellsort([-23242,-424232,-431,-1,-343,23,43023,349034]) == [-424232, -23242, -431, -343, -1, 23, 43023, 349034]

    
if __name__ == '__main__' : main()


























    
