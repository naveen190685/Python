str = "Naveen is a bad boy"
print("Below will print each character from 3 to 8")
for s in str[3:8]:
    print(s)

print("Below will print all character in str variable")
for st in str:
    print(st)

print("Prints all numbers from 0 till 8")
for i in range(9):
    print(i)

print("Print all numbers from 3 to 8")
for j in range(3, 9):
    print(j)

# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
#
# The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
#
# Hence, a for loop's else part runs if no break occurs.

digits = [3, 6, 4]
print(f'Printing digits: {digits}')
for i in digits:
    print(i)
else:
    print("digits exhausted")

###########   WHILE LOOP  ##############
print('\n\n\n\n###########   WHILE LOOP  ##############')
i, n = 0, 10
print(f'Executing while loop from i={i} to n = {n}')
while i < n:
    print(i)
    i = i + 1

# Same as with for loops, while loops can also have an optional else block.
# The else part is executed if the condition in the while loop evaluates to False.
# The while loop can be terminated with a break statement.
# In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.


c = 10
while c > 0:
    print(f'Even number: {c}')
    c = c - 1
else:
    print("c is zero now")

# A break statement will break the future iteration of a for or while loop and execution will come out
# Let say Ram gets 13 Rs daily, how many days will it take to buty 350 Rs chocolate
money = 0
for i in range(1000):
    money = money + 13
    if money >= 350:
        break

print(f'Ram can buy the chocolate in {i} days as he will be having {money} Rs')

# A continue statement will skip the current iteration of a for or while loop
# Lets say we want to print all odd numbers
print("Printing all odd number using continue in while loop")
n = 1
while n <= 15:
    if n % 2 == 0:
        n = n + 1
        continue
    else:
        print(f'{n} ')
        n = n + 1


