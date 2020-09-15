string = '*'
#     *
#    ***
#   *****
#  *******
# *********
i = 5
j = 0
while i > 0:
    print(" " * (i - 1) + string * j + string + string * j)
    j = j + 1
    i = i - 1

# *********
#  *******
#   *****
#    ***
#     *
i = 5
j = 0
while i > 0:
    print(" " * j + string * (i - 1) + string + string * (i-1))
    i = i - 1
    j = j + 1

#    *****
#    ****
#    ***
#    **
#    *

i = 5
while i > 0:
    print(string*i)
    i = i-1

#    *****
#     ****
#      ***
#       **
#        *
i = 5
j = 0
while i > 0:
    print(" " * j + string * i)
    i = i - 1
    j = j + 1

#     *
#    **
#   ***
#  ****
# *****

i = 5
j = 0
while i > 0:
    print(" " * (i-1) + string * (j+1))
    i = i - 1
    j = j + 1

# *
# **
# ***
# ****
# *****

i = 5
j = 0
while j < i:
    print(string * (j+1))
    j = j + 1