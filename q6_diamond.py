def diamond(n: int, fill: bool = True):
    r = list(range(n)) + list(reversed(range(n - 1)))
    if fill == True:
        for i in r:
            print(' ' * (n-i+1)  + '*' * (2*i+1))
    else:
        for i in r:
            print(' '*(n-i+1)  + '*' + ' '*(2*i-1) + '*'*bool(i))

diamond(5, fill=False)