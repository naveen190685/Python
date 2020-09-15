
dependencyGuide = [5, "who", 2, 4, "how"]
myString = "Just created list: {}".format(dependencyGuide)
print(myString)

# f' can be used when want to include anything other than string type
# Just need to have it in "{}" brackets
# And it will be automatically taken care
print("with F'" +f'List is {dependencyGuide}')

num = 6
print(f'Just printing the number: {num}')

#****************DIFFERENT PRINTING STYLES*****************
Class = 3
rollNumber = 34
Name = "Ram"
#   Printing with .format
print("{} is in {}th class and his roll number is {}".format(Name,Class, num))
#   Printing with f'
print(f'{Name} is in {Class}th class and his roll number is {num}')
#   Printing with % formats i.e. %s for string and %d for integer, %f for float
print("My name is %s and weight is %d kg!" % ('Zara', 21))
#   Printing with direct concatination
print("My name is " + Name + " and weight is " + str(21) + " Kg. Clas: " + str(Class) + " Rollno.: " + str(rollNumber))

#Printing a collection with seperators
print(dependencyGuide, "<-- MySeperatorAsPrefix", sep="$$")

