
def primeNumbers(n1: int, n2: int) -> list:
    if n1 < 1 or n2 < 1:
        raise Exception("Numbers should be greater than 1")
    allNums = set(range(n1, n2+1))
    compositeNums = set()
    for i in allNums:
        for j in range(2, i):
            if i%j == 0:
                compositeNums.add(i)
                break
    primeNums = allNums - compositeNums
    return list(primeNums)
    

print(primeNumbers(2, 100))