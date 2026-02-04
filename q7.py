
def secondLargestNum(l: list) -> int:
    largest = max(l)
    l.remove(largest)
    secondlargest = max(l)
    return secondlargest

print(secondLargestNum([1, 2, 6, 16]))
