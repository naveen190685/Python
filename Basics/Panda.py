import pandas as pd
import numpy as np

print("High Performance")
print("Easy to use data structures")
print("Data analysis tool")
print("Provde 3 type of data structures")
print("----- Series Objects i.e. 1D array")
print("----- DataFrame Objects i.e. 2D array")
print("----- Panel Objects i.e. Dictionary of DataFrames")

print("\n\n                    SERIES OBJECTS               ")

print("        Ways to create series object")
print(f'pd.Series([23,34,51,69]) => \n{pd.Series([23, 34, 51, 69])}')
print(
    f'Creating series with all element labels \npd.Series([4, 2, 1, 5], index=["fan", "plug", "switch", "regulator"]) => '
    f'\n{pd.Series([4, 2, 1, 5], index=["fan", "plug", "switch", "regulator"])}')
print('Creating series with dictionary {"fan": 3, "plug": 8, "switch": 4, "regulator": 3}')
print('pd.Series({"fan": 3, "plug": 8, "switch": 4, "regulator": 3} =>')
print(f'{pd.Series({"fan": 3, "plug": 8, "switch": 4, "regulator": 3})}')
print(f'Creating series object with single value to all labels')
print(f'pd.Series(42, ["plug", "switch"]) => \n{pd.Series(42, ["plug", "switch"])}')
print(f'Naming a series object')
print('pd.Series([2, 5, 1], index=["fan", "plug", "regulator"], name="Fan parts") => ')
print(f'{pd.Series([2, 5, 1], index=["fan", "plug", "regulator"], name="Fan parts")}')

n = pd.Series([2, 4, 1, 9])
print(f'Creating series object "n" using \nn = pd.Series([2,4,1,9]) => \n{n}')
print(f'Squaring all elements in series')
print(f'np.square(n) => \n{np.square(n)}')
print(f'Normal arithematic operation n+[1,2,3,4] =>\n{n + [1, 2, 3, 4]}')
print(f'Broadcasting operation n+1 =>\n{n + 1}')
print(f'Comparision n<3 => \n{n < 3}')

se = pd.Series([5, 2, 8, 6], index=["apple", "banana", "mango", "lichi"])
print(
    f'Panda series with named lables \nse = pd.Series([5, 2, 8, 6], index=["apple", "banana", "mango", "lichi"]) => \n{se}')
print(f'Accessing series with index se[1] => {se[1]}')
print(f'Accessing series with index location se.iloc[1] => {se.iloc[1]}')
print(f'Accessing series with label se["banana"] => {se["banana"]}')
print(f'Accessing series with label location se.loc["banana"] => {se.loc["banana"]}')

print("                                         \n\nCreating series with dictionaries \n")
fruits = {"apple": 3, "banana": 8, "mango": 4, "lichi": 3}
print(f'fruits = {fruits}')
fruitSe = pd.Series(fruits)
print(f'pd.Series(fruits) = \n{fruitSe}')
partialSeDic = pd.Series(fruits, index=["apple", "banana"])
print(f'Creating partial series from a dictionary pd.Series(fruits, index=["apple", "banana"]) => \n{partialSeDic}')

otherFruits = {"apple": 2, "banana": 3, "Orange": 4}
otherFruitSe = pd.Series(otherFruits)
print(f'\n\nfruits => \n{fruitSe}')
print(f'\notherFruitSe => \n{otherFruitSe}')
print(f'\nfruitSe + otherFruitSe => \n{fruitSe + otherFruitSe}')
print(f'========== Added the commons i.e. apple and banana, however others kept as NaN')

print(f'\n\n                       CREATING DATAFRAMES')
fruitDF = pd.DataFrame([fruitSe, otherFruitSe])
print(f'pd.DataFrame([fruitSe, otherFruitSe]) => \n{fruitDF}')

print(f'Creating data frame out of series objects')
people_dict = {
    "weight": pd.Series([68, 23, 43], index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1984, 1986, 1985], index=["alice", "bob", "charles"]),
    "children": pd.Series([0, 3], index=["charles", "bob"]),
    "hobby": pd.Series(["biking", "dancing"], index=["alice", "bob"])
}

people = pd.DataFrame(people_dict)
print(people)
print("\nAccesing a column e.g. 'birthyear' using \npeople['birthyear'] =>")
print(f'{people["birthyear"]}')
print(f'Adding a new column to the people dataFrame\npeople["age"] = 2017-people["birthyear"] =>')
people["age"] = 2017-people["birthyear"]
print(people)
print(f'\nAccesing a record/rows with name e.g. "bob" using: \npeople.lob["bob"] =>')
print(f'{people.loc["bob"]}')
print(f'\nAccessing a record with index e.g. \npeople.iloc[1] =>')
print(f'{people.iloc[1]}')
print(f'\npeople => \n{people}')
print(f'\nAccessing multiple rows using iloc e.g. \npeople.iloc[1:3] =>')
print(f'{people.iloc[1:3]}')
print(f'\npeople => \n{people}')
print(f'Passing boolean array to get desired rows\npeople[np.array([True, False, True])] =>')
print(f'{people[np.array([True, False, True])]}')
print(f'\npeople => \n{people}')
print(f'\nGet people with birthyear < 1990\npeople["birthyear"]<1990 =>\n{people["birthyear"]<1990}')
print(f'Storing the above genetated array in condiArray:\ncondiArray = people["birthyear"]<1990')
condiArray = people["birthyear"]<1990
print(f'Using the condiArray to get the record values\npeople[condiArray] =>\n{people[condiArray]}')
print("                   DELETING COLUMNS")
print('Delete using pop. Deletes and return the deleted column\npeople.pop("age") =>')
print(people.pop("age"))
print(f'people => \n{people}')
print('\n\nDelete using del deletes the specified column\ndel people("children") =>')
del people["children"]
print(f'people => \n{people}')
