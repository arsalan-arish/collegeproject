# Printing a pascal triangle
""" n = 6
0                   1               
1                 1   1            
2               1   2   1           
3             1   3   3   1         
4           1   4   6   4   1       
5         1   5   10   10   5   1   
6       1   6   15   20   15   6   1

Pattern:
i represents rows while j represents a column
n represents how many rows to make of the triangle
"""
n = int(input("Enter the number of rows of the pascal triangle -> "))
print()

def generate_pascal_triangle_row(n: int):
    # Getting previous row through recursion
    if n == 0:
        return [1]
    previousRow: list = generate_pascal_triangle_row(n - 1)
    # Generating this row
    totalMiddleElements = n - 1
    middleElements = []
    for i in range(totalMiddleElements):
        middleElements.append(previousRow[i] + previousRow[i+1])
    
    return [1] + middleElements + [1]

def print_pascal_triangle(n: int, kind: str):
    for i in range(n):
        # Spaces logic
        if n < 6:
            startSpaces = 4 - i
            inBetweenSpaces = 1
        elif n < 10:
            startSpaces = 2*n - 2*i
            inBetweenSpaces = 3
        # After the number of rows surpasses a bigger number like 9, the spaces logic will require to be extended to more conditional statements
        print(" "*startSpaces, end="")

        # Printing numbers
        row_numbers: list = generate_pascal_triangle_row(i)
        for num in row_numbers:
            if kind == "integers":
                print(num, end=" "*inBetweenSpaces)
            elif kind == "alphabets":
                print(chr(num + 65), end=" "*inBetweenSpaces)
            elif kind == "evenintegers":
                print(2*num, end=" "*inBetweenSpaces)
            elif kind == "oddintegers":
                print()
        print()

print(ord('a'), ord('A'))