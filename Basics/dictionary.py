#Empty dictionaries/map can be created with below statements:
almera = {}
#or
almera1 = dict()

print(f'Check if almera1 dictionary is empty: {almera1 is False}')

#Can give values while declaring as well
almera2 = {1: "cloths", "second": "articles"}
#Values can be later added as
almera[1]= "pants"
#values can be update as
almera[1]= "shirts"

#adding more to the dictionary
almera["section 2"] = "pants"
print(almera)
print(almera1)
print(almera2)
for i in almera2:
    print(i)

print(f'almera2.items(): {almera2.items()}')
print(f'almera2.keys(): {almera2.keys()}')
print(f'almera2.values(): {almera2.values()}')

d = { 'one' : 1 , 'two' : 2, 'three' : 3, 'four': 4 }
print(len(d))
print('three' in d)
print(4 in d)
print(5 in d and 2 in d)


def dict_func(myStr):
    count = 0
    wordCount = dict()
    for st in myStr.split():
        if st not in wordCount:
            wordCount[st] = 0
        wordCount[st] = wordCount[st] + 1
    print(wordCount)

dict_func('the quick brown fox jumps over the lazy dog')


