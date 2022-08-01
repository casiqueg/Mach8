# Code to create the list of integers that the user wants to compare the sum of all the tuples
# that could be equal to the number chusen by the user.
# Writen by Gabriel Casique in Python 3.

def main():
    # empty list
    intList = []
      
    # number of elements as input
    n = int(input("Enter number of elements : "))
      
    # iterating to get the list of integers complete (O(n))
    for i in range(0, n):
        element = int(input("Enter element "+str(i+1)+": "))
        intList.append(element) # adding the element
        
    # sorting the List of integers to reduce the number of cycles to O(n/2)
    intList.sort()
    print("Sorted List: ", intList)
    
    num = int(input("Number to compare with the sum of each 2 elements : "))
    results = False
    j = 0
    k = n-1
    
    # cycle that beggins with comparing the sum with the minor element with the maximum element
    # the cycle could repeat tuples of elements if the user repeats integer to include in the list.
    while j < k:
        # if the elemets compared sums the number to compare, the tuple is printed in console and
        # the next elements to compare will be the following between these current elements 
        if intList[j]+intList[k] == num:
            print(str(intList[j]), str(intList[k]))
            j += 1
            k -= 1
            results = True
        # if the sum is lower than the number to compare with, the index of the lower element
        # increments to the following 
        elif intList[j]+intList[k] < num:
            j += 1
        # if the sum is higher than the number to compare with, the index of the higher element
        # decrements to the previous 
        else:
            k -= 1
            
    # last review in case for odd lists and the previous last 'while' cycle where TRUE
    if j == k and n % 2 == 1:
        if intList[j]+intList[j-1] == num:
            print(str(intList[j-1]), str(intList[j]))
            results = True
        elif intList[j]+intList[j+1] == num:
            print(str(intList[j]), str(intList[j+1]))
            results = True
    
    # Message to print if there's no tuple that sums the number to compare with
    if not results:
        print("There's no combination that sums ", str(num)," in the list ", str(intList))

if __name__ == "__main__":
    main()
