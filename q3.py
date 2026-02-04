# 5x6
#        ******   ******   ******
#        *    *   *        *
#        ******   *  ***   *
#        *        *    *   *
#        *        ******   ******

# Now to make them all horizontal, we will collect the first lines printed by all loops into a single string
# Same for the other lines
# Then just print the strings sequentially


lines_P = []
for i in range(5):
    line = ""
    for j in range(6):
        if (i == 0 or i == 2) or (i == 1 and (j == 0 or j == 5)) or (i > 2 and j == 0):
            line += "*"
        else:
            line += " "
    lines_P.append(line)

lines_G = []
for i in range(5):
    line = ""
    for j in range(6):
        if (i == 0 or i == 4) or (i == 1 and j == 0) or (i == 2 and (j == 0 or j > 2)) or (i == 3 and (j == 0 or j == 5)):
            line += "*"
        else:
            line += " "
    lines_G.append(line)

lines_C = []
for i in range(5):
    line = ""
    for j in range(6):
        if (i == 0 or i == 4) or ((i > 0 or i < 4) and (j == 0)):
            line += "*"
        else:
            line += " "
    lines_C.append(line)


print("\n")
for p in range(5): # 5 is the number of lines to print vertically
    print(lines_P[p] + "   " + lines_G[p] + "   " + lines_C[p])