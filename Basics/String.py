myList = [5, "who", 2, 4, "how"]
str = "Just created list: {}".format(myList)
print(str)
print("Printing from index 3 to 9th place using str[3:9]")
print(str[3:9])
print("Printing the last characters using str[-1])")
print(str[len(str) - 1])
print(str[-1])
print("Printing the first character using str[0]")
print(str[0])
print("Printing character at 5th index str[5]")
print(str[5])

print("\n\n                 ******************* CHANGING CASE **********************\n")
str1 = "I am rock rocking"
# Swapping the case
print("************Swapping case")
print(str1.swapcase())
# Changing to uppercase
print("************UPPER CASE")
print(str1.upper())
# Changing to lowercase
print("************lower case")
print(str1.lower())
# print(str1.rindex("am"))

print("\n *************************** String split *************")
myStr = "I am hard working"
print(f'myStr = {myStr}')
print(f'Split to char in form of list using list(myStr): {list(myStr)}')
print(f'Split to words in form of list using split function using myStr.split(): {myStr.split()}')
print(f'Split according to a character in form of list using split function using myStr.split(): {myStr.split("hard")}')
myStr = "I am hard working. I am a coder"
print(f'Split according to a character in form of list using split function using myStr.split(): {myStr.split("am")}')

print("\n ************************** Join Strings *************************")
print(f'Storing the words in list using: myStrList = myStr.split("am")')
myStrList = myStr.split("am")
delimiter = "do"
print(f'Joining the words with delimiter {delimiter}')
print(f'delimiter.join(myStrList): {delimiter.join(myStrList)}')

print("\n\n                  ********************* PLAY AROUND **********************\n")

print("\n----------------------- Replace")
str2 = "banana"
print("str2 = \"banana\"")
print("Replacing all occurrence of n using str2.replace(\"n\",\"a\"): " + str2.replace("n", "a"))
print("Replacing 1 occurrence of n using str2.replace(\"n\",\"a\",1): " + str2.replace("n", "a", 1))

print("\n------------------------- Find")
print("Considerting str1 = \"I am rock rocking\"")
print(f'Lowest index for occurrence of rock within str1 in str.find(str1): {str1.find("rock")}')
print(f'Find the highest of index for the asked substring \"rock\" using str2.rfind(\"rock\": ): {str1.rfind("rock")}')
print(f'Highest index for occurrence of rock within str1 in str.rindex(str1): {str1.rindex("rock")}')
print(f'rfind returns -1 if not not where as rindex returns valueError')
print("For eg.")
print(f'Error for rfind when don\'t find: {str1.rfind("dd")}')
print("Error for rindex when don\'t find:")
try:
    print(f'{str1.rindex("dd")}')
except ValueError:
    print("\tValueError occured while doing str1.rindex(\"dd\")")

print("\n---------- Prefix and Postfix")
line = "Have a nice day"
print(f'line = {line}')
print(f'Check prefix using line.startswith("Have"): {line.startswith("Have")}')
print(f'Check postfix using line.endswith("day"): {line.endswith("day")}')

print("\n--------------------- Trim()")
myStr = "       my String     "
print(f'myStr: {myStr}')
print(f'Length of variable "myStr": {len(myStr)}')
print(f'Padding % to right side of myStr for lenght > myStr using myStr.rjust(40, "%"):{myStr.rjust(40, "%")}')
print(f'Padding % to left side of myStr for lenght > myStr using myStr.ljust(40, "%"):{myStr.ljust(40, "%")}')
print(f'Trim left side spaces using myStr.lstrip():{myStr.lstrip()}')
print(f'Trim right side spaces using myStr.rstrip():{myStr.rstrip()}')
print(f'Trim both side spaces using myStr.strip():{myStr.strip()}')

print("\n-------------------- Printing substring")
print(f'Print values from starting to a position str[:5]: {str[:5]}')
print(f'Print values from a position till end str[5:]: {str[5:]}')
print("str[:] will print everything: " + str[:])
print(f'Reversing the string using str[::-1]: {str[::-1]}')
print(f'When 1st index is >= 2nd returns a space.     str[4:4]: {str[4:4]}')

# i = 0
# while i < len(str):
#     print(str[i])
#     i = i+1

print("Check if a character exist in string")
fruit = "banana"
print('fruit = "banana"')
if "na" in fruit:
    print('"na" exists in ' + fruit)

print(fruit < "apple")
print(fruit < "xxxxx")


def str_list_func(str):
    temp = ""
    myRstring = ""
    delimiter = ""
    myList = str.split(" ")
    for myStr in myList:
        mysList = list(myStr)
        temp = mysList[0]
        mysList[0] = mysList[len(mysList)-1]
        mysList[len(mysList)-1] = temp
        myRstring = myRstring + " " + delimiter.join(mysList)
    return myRstring.strip()

print(str_list_func("I am rocking"))