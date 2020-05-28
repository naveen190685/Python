# Implement formula for compount interest: (principle * rate * years) / 100


def compound_interest(principle, rate, years):
    old_principle = principle
    for i in range(years):
        principle = (principle * rate) / 100 + principle
    return principle - old_principle


print(f' All amount: {compound_interest(2500000, 10, 5)}')
print((2500000 * 5 * 11) / 100)


def str_func(var):
    if not isinstance(var, str):
        var = str(var)
    return "' + var[len(var) - 1] + '"

print(len("cloudxlab"))

#See the type printed for a function
print(type(str_func))

def funcNoReturn():
    s = 10
see = funcNoReturn()
print("A no parameter function give None is assign it to some variable")
print(see)


def conditional_statements(num1, num2, num3, num4):
    if num3<num1<num2 and num1 == num4:
        if num3<num1 and num3<num2 and num3<num4:
            if isinstance(num3, float):
                if isinstance(num1, int) and isinstance(num2, int) and isinstance(num4, int):
                    return num1+num2+num3+num4
    else:
        return None

