from symbol import for_stmt
from traceback import format_list
dependencyGuide = [5, "who", 2, 4, "how"]
print(f'myList = {dependencyGuide}')

#Appending elements to the list
print("Appended list")
dependencyGuide.append(8)
dependencyGuide.append("where")
print(f'myList: {dependencyGuide}')

#Take out some element by index
list = [2,4,8,1,0,9,6]
del dependencyGuide[3]
#Trying to pop out "where" from the list
#as pop out just happened at index 2 the index of "where"
#is updated from 6 to 5
dependencyGuide.pop(5)
print("After pop out from list")
print(f'myList: {dependencyGuide}')

#Delete a known element
list =["abd", "cdi", "dlf"]
list.remove("cdi") # This returns None

#Merging lists
mySecList= ["k", 3, 9, "u"]
print(f'New list: {mySecList}')
dependencyGuide = dependencyGuide + mySecList
print("Merged List:")
print(f'myList = {dependencyGuide}')

#Sorting list
myNumericList = [3,4,8,2,0]
# The sort() method returns None so below command will turn myNumericList to None instead of the list just assigned
myNumericList = myNumericList.sort()
print(f'myNumericList = myNumericList.sort()\nmyNumericList = {myNumericList}')

myNumericList = [3,4,8,2,0]
#However, the sorted() method returns list sorted in ascended order
myNumericList = sorted(myNumericList)
print(f'myNumericList = sorted(myNumericList)\nmyNumericList = {myNumericList}')

myNumericList = [3,4,8,2,0]
#However, the sorted() method can also return list sorted in descending order
myNumericList = sorted(myNumericList, reverse=1)
print(f'myNumericList = sorted(myNumericList, reverse=1)\nmyNumericList = {myNumericList}')

# Method sort() sorts in ascending order and modify the list so no need to assign
myNumericList = [3,4,8,2,0]
myNumericList.sort()
print(f'Sorted list myNumericList: {myNumericList}    default order: Ascending')
myNumericList.sort(reverse=1)
print(f'Sorted list descending order: {myNumericList}')

myNumericList = [3,4,8,2,0]
myNumericList.reverse()
print(f'Reversed list: {myNumericList}')
print(f'Sorted List: {sorted(myNumericList)}')
print((0,1,200000)<(0,3,4))  #this returns true
print((0,1,200000)>(0,3,4))  #this returns false          WHY?????????????

a = [23,12,32,1,2,34,56]
# append to last position
a.append(12)
print(a[len(a)-2])

#Appending a to a
a.extend(a)
print(a)

def getTotal(a):
    total = 0
    for n in a:
        total = total + n
    print(total)

list = [12,23,43,[2,4,5], 2, 4,5]
list.pop(3)
getTotal(list)

list = ['cloudx', 'lab', 'provides', 'cloud', 'lab']
del list[:]
print(len(list))

list = ['cloudx', 'lab', 'provides', 'cloud', 'lab']
print("Accessing list with list[1:]")
print(list[1:])
print("Accessing list with list[1][2]")
print(list[1][2])
print("Accessing like below is not allowed in python")
try:
    print(list[2, 4])
except TypeError:
    print("\t\tType Error exception occured when calling with [2, 4]")



