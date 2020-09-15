myArray = [23, 33, 23, 78, 87, 78, 56, 67, 23]
print(myArray)
# Eliminate the duplicates
uniqueArray = []
for e in myArray:
    if e not in uniqueArray:
        uniqueArray.append(e)
print("Unique elements => " + str(uniqueArray))

# Get duplicate elements
# method #1
duplicates = []
elements = {}
for e in myArray:
    if e not in elements.keys():
        elements[e] = 1
    else:
        elements[e] = elements[e] + 1
for e in elements.keys():
    if elements[e] > 1:
        duplicates.append(e)
print(elements)
print(duplicates)

# method #2
duplicates = []
for i in range(0, len(myArray)):
    for j in range(i+1, len(myArray)):
        if myArray[i] == myArray[j] and myArray[i] not in duplicates:
            duplicates.append(myArray[i])
print(duplicates)

#  ROTATE AN ARRAY
myArray = [3, 2, 1, 4, 5]
# change this to [4, 5, 1, 3, 2]
center = int(len(myArray)/2)
i = 0
Right = []
Left = []
while i < center:
    Right.append(myArray[i])
    i = i + 1
i = i + 1
while i < len(myArray):
    Left.append(myArray[i])
    i = i+1
Left.append(myArray[center])
newArray = Left + Right
print(newArray)



