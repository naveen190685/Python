import numpy as np
tup_dim = (3, 4)

array=[2,3,5,7,8,9]
print(f'array: {array}')
print(f'Jumping array starting index 2nd position to every 2nd element using array[2::2]: {array[2::2]}')
print(f'Jumping array starting index 0th position to every 3nd element array[0::3]: {array[0::3]}')
print(f'Revesing the array using array[::-1]: {array[::-1]}')

print("Converting a simple array to numpy array with np.array(<yourArray>)")
array = np.array(array)
print(array)

print("*****************Assigning -1 to index 1 to 3rd position of a numpy array by doing array[1:3] = -1")
array = np.array(array)
array[1:3] = -1
print(array)

my_reshaped_array = np.reshape(array,(2,3))
print("******************Reshaping the array to 2 x 3 matrix using np.reshape(array,(2,3))")
print(my_reshaped_array)

print("\n\n*******************************Slicing the array, original array get impacted example")
array = np.array([1,2,5,7,8])
print(f'Original array: {array}')
print(f'Taking a slick array[1:5], array_slice = ')
array_slice = array[1:5]  # i.e. 2,5,7,8
print(array_slice)
print("Updated the value at index 1 of the slice i.e. array_slice[1] = 1000")
array_slice[1] = 1000   # 2, 1000, 7, 8
#Check array now if it is impacted
print(f'Original np array i.e. array got affected: {array}')

print("\n\n********************************Slicing the array, with no impact on original example")
array = np.array([1,2,5,7,8])
print(f'Original array: {array}')
print(f'Taking a slick copy using array[1:5].copy(), another_slice = ')
another_slice = array[1:5].copy()
print(another_slice)
print("Updated the value at index 1 of the slice i.e. another_slice[1] = 1000")
another_slice[1] = 1000
print(f'Original not affected: {array}')

#Accessing an array
print("\n\n**********************  ARRAY ACCESS EXAMPLES **************************\n")
print("Defining new array with np.array([ [2, 4, 6], [1, 3, 5] ])")
array = np.array([
    [2, 4, 6],
    [1, 3, 5]
])
print(array)
#Two ways to access a element in array i.e. either with comma or boxes
print(f'The of array at position 2nd row and 3rd column with command array[1,2] is: {array[1,2]}')
print(f'The of array at position 2nd row and 3rd column with command array[1][2] is: {array[1][2]}')

my_zeros_array = np.zeros(tup_dim, dtype=np.int16)
print("Note: tup_dim is a tuple with valus (3,4)")
print("Creating zero array with np.zeros(tup_dim, dtype=np.int16): ")
print(my_zeros_array)


my_ones_array = np.ones(tup_dim, dtype=np.int16)
print("Creating ones array with np.ones(tup_dim, dtype=np.int16): ")
print(my_ones_array)
#
my_seven_array = np.full(tup_dim, 7, dtype=np.int16)
print("Print seven array with np.full(tup_dim, 7, dtype=np.int16): ")
print(my_seven_array)

my_identity_array = np.identity(2, dtype=np.float64)
print("MY IDENTITY ARRAY, i.e. square bracket with also 0 but corner elements as 1")
print("np.identity(2, dtype=np.float64): ")
print(my_identity_array)

# NumPy array with all its elements values as random values (using random.rand() function of NumPy())
my_rand_array = np.random.rand(3, 4)
print("Creating random array with np.random.rand(3, 4)")
print(my_rand_array)

# NumPy array with all its elements values as uninitialized values (initialized with some random values
# which you are not aware of - using empty() function of NumPy)
my_uninitialized_array = np.empty(tup_dim, dtype=np.float64)
print("Printing uninitialized array using np.empty(tup_dim, dtype=np.float64):")
print(my_uninitialized_array)

# Creating a NumPy array by passing a range of values (using arange() function of NumPy
my_range_array = np.arange(10, 30, 5)
print("Using arange function to print numbers between 10 to 30 with a gap of 5 without including 30")
print("Here the gap is controlled, , Not the number of values to be printed")
print("np.arange(10, 30, 5): ")
print(my_range_array)

# Creating a NumPy array by passing an equally spaced range of values (using linspace() function of NumPy)
my_spaced_array = np.linspace(0, 5/3, 6)
print("Using linspace function to print 6 numbers between 0 to 5/3 with equal gap between them")
print("Here the number of values is controlled, no the gap. However gap is kept constant by default")
print("np.linspace(0, 5/3, 6): ")
print(my_spaced_array)

my_array = np.array([ [1, 4, 5, 6], [7, 8, 9, 10], [11, 12, 14, 16] ])
print(f'Created numpy array\n my_array: \n{my_array}')

print(f'*********************The total dimensions of the array, \nmy_array.ndim : {my_array.ndim}')
print(f'*********************The dimensions of the array (in tuple),\nmy_array.shape : {my_array.shape}')
print(f'*********************The total size of array\nmy_array.size: {my_array.size}')
print(f'*********************The data type of the items in array\nmy_array.dtype: {my_array.dtype}')
print(f'*********************The size of each array element in bytes\nmy_array.itemsize: {my_array.itemsize}')

print("                                     PERFORMING ARITHMETIC OPERATIONS                                 ")
print("******** Guess the missing array")
array=np.array([[2,6], [5,3]])
print("array: \n"+str(array))
result = np.array([6,-9])
print("result:\n"+str(result))
from numpy import linalg
missingArray=linalg.solve(array,result)
print("Solving the missing array with linalg.solve(array,result):")
print(missingArray)
print("Checking back the result by multiplying array to missingArray i.e. array.dot(missingArray)")
print(array.dot(missingArray))
