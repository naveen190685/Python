from symbol import for_stmt
from traceback import format_list

# You cannot merge, append, sort, reverse a tuple
myTuple = (5, "who", 2, 4, "how")
print("Just created tuple")
# print('Just created list'.join(myTuple))
print("myTuple = ")
print(myTuple)

print("You can have tuple on the left-hand side of the assignment as well.")
print(f'myList = [1,2,3]')
myList = [1, 2, 3]
print(f'(a,b,c) = myList')
(a, b, c) = myList
print(f'Values in tuple (a, b, c) = {(a, b, c)}')
print(f'Below is also valid')
print(f'\td, e, f = myList')
d, e, f = myList
print(f'Values in tuple d, e, f = {d, e, f}')

print(f'For swapping a, b we can also do')
print(f'\ta, b = {a, b}')
print(f'\t a, b = b, a')
a, b = b, a
print(f'\ta, b is now= {a, b}')

print(f'Define a single member tuple: tup = ("na",)')
tup = ("na",)
t = (1)
print(type(t))

print(f'Declaring a tuple without values: emptyTup = tuple()')
emptyTup = tuple()
print(type(emptyTup))
print(emptyTup)

t1 = tuple("1,2,3,4,5")
t2 = tuple([1, 2, 3, 4, 5])
t3 = tuple((1, 2, 3, 4, 5))
print(t1)
print(t2)
print(t3)

t = (1, 3, 5, 2, 54, 34, 2, 34, 5)
t2 = t[2:5]
t3 = t[1:3] + t2[:]
count = 0
for val in t3:
    count = count + val
print(f'Count: {count}')

print("Python compares the tuples element-wise starting with the 1st element.\n"
      "If they turn out to be equal, it proceeds to the next one.\n"
      "If it finds any difference in elements, it gives the result without considering the further elements.")
print(f'(0, 1, 2) < (0, 3, 4) : {(0, 1, 2) < (0, 3, 4)}')
print(f'(0, 1, 2) < (0, 3): {(0, 1, 2) < (0, 3)}')
print("For above example. It doesn't depend on the number of elements in each tuple.\n"
      "It is only concerned with the two elements that it is comparing at one time.")

lis = [(0, 23, 34), (2, 34, 23), (1, 34, 23)]
print(f'Created list of tuples -> lis = {lis}')
lis.sort()
print(f'Sorted lis: {lis}')
lis.sort(reverse=True)
print(f'Reverse sorted lis: {lis}')
# print(sorted(l))


print("No changes is possible on Tuple type")
print("you can't perform merger, adding or deleting items")
print("In short no updation possbile in tuple once created")
print("Because they are unmutable")

# All below operation will give error if you try

# t = (1,3,5,2,54,34,2,34,5)
# t.sort()
# print(f'Sorted t: {t}')
# t.sort(reverse = True)
# print(f'Reverse sorted t: {t}')

# #Appending elements to the tuple
# print("Append 8 and 'where' to the tuple")
# myTuple.append(8)
# myTuple.append("where")
# print(myTuple)
#
# #Taking out an element from typle
# myTuple.pop(2)
# print("Taken out element 2 from the typle myTuple")
# print(myTuple)
#
# #Merging lists
# print("Merging lists****************")
# mySecTuple= ["k", 3, 9, "u"]
# print("Second list mySecTuple")
# print(mySecTuple)
# myTuple = myTuple + mySecTuple
# print("Merged Tuple:")
# print(myTuple)
