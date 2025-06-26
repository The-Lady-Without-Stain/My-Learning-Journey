#BROADCASTING
import numpy as np
A = np.array([1, 3, 4])
B = np.array ([[3], [4]])
#print(A+B)

a = np.random.random((2, 3, 1, 5, 6, 1, 1, 7))
b = np.random.random((2, 1, 6, 5, 1, 8, 9, 1))
#print(a+b)
#print((a+b).shape)

#ADVANCED INDEXING
Ami = np.random.randint(10,30, size = (6, 5))
#print(Ami)
#print(Ami[2,:])   #Using colon (:) means give me everything
#print (Ami[:, 1, np.newaxis])     #Newaxis gives the outputs separate lists vertically instead of in one list
#print (Ami[np.newaxis, :, 1])     #This gives a horizontal output
#print(Ami[[2, 1]])            #This means give me row 1 and row 2

#print(Ami[[3, 4], [2, 1]])      #The element in cell R3C2 and R4C1
#print(Ami[[3, 2, 2], [2, 4, 1]])      #The element in cell R3C2 and R2C4 and R2C1

#SORTING
#print(np.sort(Ami))           #Sorts the elements list by list,  but does not change the original list
#a.sort()
#print(np.sort(Ami, axis=1))     #Sorts row by row
#print(np.sort(Ami, axis = 0))      #Sorts column by column
#print(np.sort(np.sort(Ami, axis = 0), axis = 1))    #Sorts by rows and columns

#SEARCHING
sam = np.array([2, 4, 6, 0, 8, 7, 9, 12, 0, 1])
print(np.argmax(sam))
print(np.argmin(sam))
print(np.nonzero(sam))