# Pattern of name
name: str = "MUHAMMAD ATIF"

for i in range(len(name)):
    print(name[:i+1])

# As a pyramid
n = int(len(name)/2)+1
for i in range(n):
    print(" "*(n-i), end="")
    print(name[:2*(i+1)-1])