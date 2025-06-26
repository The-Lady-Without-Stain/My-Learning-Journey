import numpy as np
print (np.__version__)

arr = np.arange(26)
print(type(arr))
print (arr)
#To assess a particular number, we use indexing like the examples below
print(arr[6])
print(arr[18])
      
#checks the run time of your code

Listt = list(range(1000001))
for l in Listt:
    Listt[l] * Listt [l]
mult = Listt[l] * Listt [l]
print(mult)

varr = np.arange(1001)
print(type(varr))
print(varr)
#Indexing
print(varr[106])
print(varr[68])

Ones= np.ones((4,6))
print (Ones)
print(Ones.shape)
print(Ones.dtype)
print(Ones.ndim)
print(Ones.itemsize)

Zeroes= np.zeros((3,2))
print(Zeroes)

Matrix= np.eye(6,6)
print(Matrix)

Arr_str = np.array([2,3,5,7,6,8], dtype = 'str')
print(Arr_str)

#NUMPY PYTHON NUMBERS
#rand --> Generates a specified number of random numbers between 0 and 1
Rand= np.random.rand(6)
print(Rand)

Rand_2= np.random.rand(6,2)
print(Rand_2)

#randint--> Generates one single number between a specofied range
Randint= np.random.randint(12)
print(Randint)

Randint_2= np.random.randint(12, size = (6,3))
print(Randint_2)

Randint_3= np.random.randint(4, 24, size = (4,5))
print(Randint_3)

#Uniform--> Generates a single positive number
Randuni= np.random.uniform(12)
print(Randuni)

Randuni_2= np.random.uniform(5, 10,  size = (4,4))
print(Randuni_2)
#Indexing
print(Randuni_2[2])
print(Randuni_2[2,3])
print(Randuni_2[[0,1], [1,2]]) #the first list is specifying rows and the second is specifying columns

#SLICING: Use column to retrieve a range of numbers
My_arr = np.random.randint(21, size = (12,5))
print(My_arr)
print(My_arr[1:7])  #slicing from the 2nd number to the 7th
print(My_arr[4:-4])    #slicing from the 5th number to the 5th number from the back
print(My_arr[::3])        #retrieves numbers from your array in steps of 3
print(My_arr[0:2, 1:3])    #Using 2 way assessing

#Indexing with booleans
Barr= np.random.randint(10, size = (10,))
print(Barr)
index = [True, False, True, True, False, True, False, True, False, False]
print(Barr [index])

#UPDATING in numpy arrays
Purr= np.random.randint(60, size = (4, 2))
print('Original array: \n', Purr)

Purr[1,1] = 55
print('Updated array: \n', Purr)


#NUMPY FLATTEN AND RAVEL
array = np.random.randint(25, size = (6,4))
print('Array: \n', array)
print('Shape: \n', array.shape)

flattened_array = array.flatten()
print('New Array: \n', flattened_array)
print('Shape: \n', flattened_array.shape)
ravel_array = array.ravel()
print('Ravel Array: \n', ravel_array)

#the difference between flatten and ravel is that any changes made to the flattened array does not affect the original one
#while changes made to the raveled array affects the original array

#NUMPY RESHAPE
arrray = np.random.randint (50, size = (8, 6)) 
print("Normal Array: \n", arrray)
reshaped = arrray.reshape(6, 8)
print('Reshaped Array: \n', reshaped)
reshaped_2 = arrray.reshape (4, 12)
print('Second Reshaped Array: \n', reshaped_2)

#Iterating over numpy arrays
arr1 = np.random.randint (10,49, size = (10,))
print("Array: \n", arr1)
print("Shape: \n", arr1.shape)
for n in arr1:
    print (n, sep = ",")       #or use "for n in arr1: print (n, end = " ")


arr2 = np.random.randint (10,49, size = (10,5))
print("Array: \n", arr2)
print("Shape: \n", arr2.shape)
for row in arr2:
    print(row)

for item in arr2.ravel():
    print(item, end= " ")


#Write a program that generates an array with shape 5 by 4 at random containing positive integers. 
#Perform an update by replacing all odd numbers with -1 using a loop
my_array = np.random.randint (100, size = (5, 4))
print("My Original Array: \n", my_array)
for item in np.nditer(my_array, op_flags= ["readwrite"]):
    if item %2 != 0:
        item[...] = -1
print("My Updated Array: \n", my_array)


#Python Operators on Numpy arrays
b = np.array([[2,3,5,6,9], [6,7,2,3,1]])
print("Array: \n", b)
print(b+6)
print(b*3)
print(b%2)
print(b>=6)
print(b//2)

#Exercise 2: Writw a program that generates an array with shape 5 by 4 at random containing positive integers.
#Perform an update by replacing all  odd numbers with -1 without using a loop

#Exercise 3: Write a program to filter the values from an array based on below conditions:
#1. Value should be divisible by 5
#2. value should be an odd number and a factor of 7
