
for i in range(1, 5+1):
    # spaces
    print(" "*(5-i), end="")
    
    # left
    for l in range(i, i+(i-1)):
        print(l, end="")

    # middle
    print(2*i - 1, end="")

    # right
    for r in range(i+(i-2), i-1 , -1):
        print(r, end="")

    print()


    