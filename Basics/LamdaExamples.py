#Lambda to add two numbers
add = lambda a, b: a + b
print(f'Add: {add(10, 20)}')


#Lambda in a function
def compound_interest(principle, rate, years):
    getPperY = lambda p, r: (p*r)/100
    old_principle = principle
    for i in range(years):
        principle = getPperY(principle, rate) + principle
    return principle-old_principle


print(f'Compound Interest: {compound_interest(100000, 11, 5)}')