# 5x6
#        ******   ******   ******
#        *    *   *        *
#        ******   *  ***   *
#        *        *    *   *
#        *        ******   ******

# Print P
for i in range(5):
    for j in range(6):
        if (i == 0 or i == 2) or (i == 1 and (j == 0 or j == 5)) or (i > 2 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# Print G
for i in range(5):
    for j in range(6):
        if (i == 0 or i == 4) or (i == 1 and j == 0) or (i == 2 and (j == 0 or j > 2)) or (i == 3 and (j == 0 or j == 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# Print C
for i in range(5):
    for j in range(6):
        if (i == 0 or i == 4) or ((i > 0 or i < 4) and (j == 0)):
            print("*", end="")
        else:
            print(" ", end="")
    print()