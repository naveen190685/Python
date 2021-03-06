height = 1.7
weight = 72.25
bmi = weight/(height*height)

print(int(bmi))
print(float(bmi))
print(str(bmi))

#String to list of char conversion
s = "naveen Kumar"
dependencyGuide = list(s)
print(dependencyGuide)

#String to list of word conversion
s = "Naveen Kumar"
dependencyGuide = s.split()
print(dependencyGuide)

print(f'\n******** Converting list to tuple')
#Converting a list to tuple
dependencyGuide = ["Naveen", "Kumar"]
print(f'myList = {dependencyGuide}')
print(f'(firstName, lastName) = myList')
(firstName, lastName) = dependencyGuide
print(f'(firstName, lastName) = {(firstName, lastName)}')

print("\n************* Dictionary to List of tuples")
#Converting a dictionary to list of tuples
d = {"one" : 1, "two" : 2, "three" : 3}
print(f'd = {d}')
print(f'k = d.items()')
k = d.items()
print(f'That gives k = {k}')
print(f'l = list(k)')
l = list(k)
print(f'That gives l = {l}')
for key, value in list(k):
    print(key, value)

# Define a function with the name dict_tuple_func that takes a list of integers as an argument.
# It should create a dictionary with the key as the integer and the value as the number of times it is present in the list.
# It should return a tuple in which the first element is the dictionary (you created above step) and the second element is the sum of all unique integers in the list
def dict_tuple_func(listInt):
    count = 0
    sumUnique = 0
    d = dict()
    for n in listInt:
        if n not in d:
            d[n] = 0
        d[n] = d[n] + 1
    for m in d:
        # if d[m] ==1:
            sumUnique = sumUnique + m
    return d, sumUnique

print(dict_tuple_func([1, 4, 2, 3, 1, 3, 7]))



