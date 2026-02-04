#1. Write a python program that takes a word from the user and prints the word in reverse order.
name: str = input("Enter the name -> ")
reverse: str = name[::-1]
print(reverse)